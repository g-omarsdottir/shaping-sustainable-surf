from django.shortcuts import render, redirect, reverse
from django.shortcuts import get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.db.models import Prefetch
import json

import stripe

from .forms import OrderForm
from .models import Order, OrderItem
from products.models import Product
from cart.models import DiscountCode
from cart.contexts import cart_contents


@require_POST
def cache_checkout_data(request):
    """
    Caches customer information and order details
    if the "Save Info" checkbox is checked on the checkout form.
    If so, it collects the customer's information and cart content
    and passes the data to the Stripe Payment Intent.

    Parameters:
        request (django.http.HttpRequest): The HTTP request object
                                            containing the checkout form data.

    Returns:
        django.http.HttpResponse: An HTTP response indicating success

    Raises:
        Exception: If an error occurs during the process,
                    an error message is displayed to the user.
    """

    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            "cart": json.dumps(request.session.get("cart", {})),
            "save_info": request.POST.get("save_info"),
            "username": request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        error_message = ("Sorry, your payment cannot be processed right now. "
                         "Please try again later.")
        messages.error(request, error_message)
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    View to handle the checkout process.

    GET:
    - Renders the checkout page with an empty order form.
    - Creates a Stripe PaymentIntent for the current cart total.
    - Passes Stripe public key and client secret to the template.

    POST:
    - Processes the submitted order form.
    - Creates an Order instance with form data.
    - Applies discount code if present in the session.
    - Creates OrderItem instances for each product in the cart.
    - Updates order total.
    - Redirects to checkout success page on successful order creation.

    Handles various scenarios:
    - Empty cart: Redirects to tutorials list with an error message.
    - Invalid form: Redisplays the form with error messages.
    - Product no longer available: Deletes the order and redirects to cart.
    - Missing Stripe public key: Displays a warning message.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: Renders the checkout template with context including
                      order form, Stripe public key, and client secret.
        HttpResponseRedirect: Redirects to checkout success or cart view
                              based on the outcome of the checkout process.

    Raises:
        None, but catches and handles Product.DoesNotExist exception.
    """

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

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

            # Get the discount information from the cart contents
            current_cart = cart_contents(request)
            discount_code = request.session.get("discount_code")

            if discount_code:
                try:
                    discount = DiscountCode.objects.get(code=discount_code)
                    order.discount_code = discount
                except DiscountCode.DoesNotExist:
                    messages.error(
                        request, "The discount code in your cart is not valid."
                    )
                    request.session.pop("discount_code", None)
            order.save()
            for item_id, quantity in cart.items():
                try:
                    product = Product.objects.get(id=item_id)
                    order_item = OrderItem(
                        order=order,
                        product=product,
                        product_name=product.name,
                        product_price=product.price,
                    )
                    order_item.save()
                except Product.DoesNotExist:
                    messages.error(
                        request,
                        "One of the products in your cart "
                        "is no longer available. "
                        "Please contact us for assistance.",
                    )
                    order.delete()
                    return redirect(reverse("view_cart"))
            order.update_total()
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse(
                "checkout_success", args=[order.order_number])
            )
        else:
            messages.error(
                request,
                "There was an error with your form. "
                "Please double check your information.",
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
        # Pass the discount code to the stripe payment intent
        metadata={
            "cart": json.dumps(request.session.get("cart", {})),
            "discount_code": request.session.get("discount_code", ""),
            "save_info": request.session.get("save_info", ""),
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

    template = "checkout/checkout.html"

    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    View to handle successful checkouts.
    Fetches the Order with related DiscountCode and all associated OrderItems
    with their Products in a single optimized query.
    Clears the cart and discount code from the session.
    Displays a success message and renders the checkout success template.

    Args:
        request (HttpRequest): The request object.
        order_number (str): The unique identifier for the order.

    Returns:
        HttpResponse: Renders the checkout success template
                        with the order context.
    """

    save_info = request.session.get("save_info")
    order = get_object_or_404(
        Order.objects.select_related("discount_code").prefetch_related(
            Prefetch(
                "items", queryset=OrderItem.objects.select_related("product")
            )
        ),
        order_number=order_number,
    )

    success_message = (
        f"Order successfully processed! "
        f"Your order number is {order_number}. A confirmation "
        f"email will be sent to {order.email}."
    )
    messages.success(request, success_message)

    if "cart" in request.session:
        del request.session["cart"]

    if "discount_code" in request.session:
        del request.session["discount_code"]

    template = "checkout/checkout_success.html"

    context = {
        "order": order,
    }

    return render(request, template, context)
