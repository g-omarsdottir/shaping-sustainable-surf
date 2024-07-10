import stripe
from django.http import HttpResponse
import json
import time

from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email.
        """

        cust_email = order.email
        subject = render_to_string(
            "checkout/confirmation_emails/confirmation_email_subject.txt",
            {"order": order})
        html_body = render_to_string(
            "checkout/confirmation_emails/confirmation_email_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL})

        text_body = strip_tags(html_body)

    def _send_confirmation_email(self, order):
        """
        Send the user a confirmation email
        """
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event.
        """
        intent = event.data.object

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Create or update the UserProfile model
            if save_info checkbox is selected.
        Unlock video in UserProfile model.
        """

        intent = event.data.object
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        discount_code = intent.metadata.get("discount_code")
        user_id = intent.metadata.get("user_id")
        username = intent.metadata.get("username")
        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
        billing_details = stripe_charge.billing_details
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the billing details
        for field, value in billing_details.address.items():
            if value == "":
                billing_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.get("username")
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_full_name = billing_details.name
                profile.default_phone_number = billing_details.phone
                profile.default_country = billing_details.address.country
                profile.default_postcode = billing_details.address.postal_code
                profile.default_town_or_city = billing_details.address.city
                profile.default_street_address1 = billing_details.address.line1
                profile.default_street_address2 = billing_details.address.line2
                profile.default_county = billing_details.address.state
                profile.save()

        # Check if order exists or else create the order.
        order_exists = False
        attempt = 1
        while attempt <= 10:
            try:
                order = Order.objects.get(
                    full_name__iexact=billing_details.name,
                    user_profile=profile,
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
            self._send_confirmation_email(order)
            return HttpResponse(
                content=f"Webhook received: "
                f"{event["type"]} | SUCCESS: "
                f"Verified order already in database",
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    user_profile=profile,
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
        self._send_confirmation_email(order)
        self._unlock_video_for_user(user_id)
        # Create the order
        return HttpResponse(
            content=f"Webhook received: "
            f"{event["type"]} | SUCCESS: Created order in webhook",
            status=200,
        )

    def _unlock_video_for_user(self, user_id):
        """
        Unlock the video in UserProfile model.
        """
        if user_id:
            profile = UserProfile.objects.get(user_id=user_id)
            profile.unlock_video()

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """

        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )
