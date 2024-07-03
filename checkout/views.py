from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from cart.contexts import cart_contents

import stripe


def checkout(request):
    """
    View to render the checkout page.
    Passes the context incl. stripe API keys to the template.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    template = "checkout/checkout.html"

    order_form = OrderForm()

    if request.method == "POST":
        cart = request.session.get("cart", {})

        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST["street_address2"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "county": request.POST["county"],
            "country": request.POST["country"],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product_id = int(item_id[0])  # Extract the first element of the tuple and convert it to integer
                    product = Product.objects.get(id=product_id)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                    )
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request, "One of the products in your cart "
                        "is no longer available. "
                        "Please contact us for assistance."
                    )
                    order.delete()
                    return redirect(reverse("view_cart"))
            order.update_total()
            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                reverse("checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request, "There was an error with your form. "
                "Please double check your information."
            )
    
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(
                request, "There is nothing in your cart at the moment"
            )
            return redirect(reverse("tutorials_list"))

    current_cart = cart_contents(request)
    total = current_cart["grand_total"]
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
        automatic_payment_methods={
            "enabled": True,
        },
    )

    if not stripe_public_key:
        messages.warning(
            request,
            (
                "Stripe public key is missing. "
                "Did you forget to set it in "
                "your environment?"
            ),
        )

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View to handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    messages.success(request, f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.")

    if "cart" in request.session:
        del request.session["cart"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)