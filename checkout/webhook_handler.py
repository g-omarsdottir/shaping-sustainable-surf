import stripe
from django.http import HttpResponse
import json
import time

from django.contrib.auth.models import User

from .models import Order, OrderItem
from products.models import Product
from cart.models import DiscountCode
from profiles.models import UserProfile


class StripeWH_Handler:
    """
    Handle Stripe webhooks.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        """
        intent = event.data.object

        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Unlock video in UserProfile model.
        """

        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        discount_code = intent.metadata.get("discount_code", "")
        user_id = intent.metadata.get("user_id", "")
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        # Check if order exists or else create the order.
        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    # user_profile=profile,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    country__iexact=billing_details.address.country,
                    postcode__iexact=billing_details.address.postal_code,
                    town_or_city__iexact=billing_details.address.city,
                    street_address1__iexact=billing_details.address.line1,
                    street_address2__iexact=billing_details.address.line2,
                    county__iexact=billing_details.address.state,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(2)
        if order_exists:
            self._unlock_video_for_user(user_id)
            #self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=billing_details.name,
                    email=billing_details.email,
                    phone_number=billing_details.phone,
                    street_address1=billing_details.address.line1,
                    street_address2=billing_details.address.line2,
                    postcode=billing_details.address.postal_code,
                    town_or_city=billing_details.address.city,
                    county=billing_details.address.state,
                    country=billing_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        product_name=product.name,
                        product_price=product.price,
                    )
                    order_item.save()
                # Handle discount code
                if discount_code:
                    try:
                        discount = DiscountCode.objects.get(code=discount_code)
                        order.discount_code = discount
                        order.save()
                    except DiscountCode.DoesNotExist:
                        pass
                order.update_total()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )
        #self._send_confirmation_email(order)
        self._unlock_video_for_user(user_id)
        # Create the order
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200,
        )

    def _unlock_video_for_user(self, user_id):
        """
        Unlock the video in UserProfile model.
        """
        if user_id:
            try:
                profile = UserProfile.objects.get(user_id=user_id)
                profile.unlock_video()
                print(f"Unlocked video for user {profile.user.username}")
            except UserProfile.DoesNotExist:
                print(f"UserProfile for user_id {user_id} not found")
            except Exception as e:
                print(f"Error unlocking video: {str(e)}")

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)
