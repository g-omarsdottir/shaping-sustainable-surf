from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


@login_required
def profile(request):
    """
    Display the user profile, order history,
    and tutorials according to video unlock status
    and profile form.
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile)

    context = {
        "form": form,
        "profile": profile,
        "on_profile_page": True,
        "orders": orders,
    }
    template = "profiles/profile.html"

    return render(request, template, context)


@login_required
def delete_profile(request):
    """
    Delete the user profile and associated user account.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    # Perform the deletion
    if request.method == "POST":
        user = request.user
        profile = get_object_or_404(UserProfile, user=user)

        # Delete the user profile
        profile.delete()

        # Delete the user account
        user.delete()

        messages.success(
            request,
            "Your profile and user account have been successfully deleted."
        )
        return redirect(reverse("home"))

    # Render a confirmation page for deletion
    else:
        context = {
            "profile": profile,
        }

        template = "profiles/profile_confirm_delete.html"

        return render(request, template, context)


@login_required
def order_history(request, order_number):
    """
    Checks if user is authorised to view order history.
    Display the order history to authenticated user.
    """

    order = get_object_or_404(Order, order_number=order_number)

    if order.user_profile.user != request.user:
        raise PermissionDenied

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
