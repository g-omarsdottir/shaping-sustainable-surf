from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from checkout.models import Order


def profile(request):
    """
    Display the user profile, order history, and
    tutorials according to video unlock status.
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")

    context = {
        "profile": profile,
        "orders": orders,
    }
    template = "profiles/profile.html"

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f"This is a past confirmation for order number {order_number}. "
        "A confirmation email was sent on the order date."
    ))

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
