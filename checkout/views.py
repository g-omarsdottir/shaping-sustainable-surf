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

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(
            request, "There's nothing in your cart at the moment"
        )
        return redirect(reverse("tutorials"))

    order_form = OrderForm()

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            
            # Process payment and complete order
            # Create order items
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                order_item = OrderItem(
                    order=order,
                    product=product,
                )
                order_item.save()

            # Redirect to a success page
            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(
                request, "There was an error with your form. "
                "Please double check your information."
            )

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
