from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from allauth.account.models import EmailAddress

from .models import UserProfile
from .forms import UserProfileForm
from checkout.models import Order


def send_notification(old_email, new_email, user, profile):
    """
    Function to send notification by email
        if the email address of a user account is changed.
    Notification is sent to the old and the new email address.
    In case of a failure,
        fails silently to avoid breaking the user experience.
    Args:
        old_email (str):
            previous auth.EmailAddress. associated with the user account.
        new_email (str):
            new auth.EmailAddress. the user has changed to.
        user (auth.User):
            User instance of the account.
        profile (profile.UserProfile):
            The UserProfile instance associated with the user.
    """
    from_email = settings.DEFAULT_FROM_EMAIL
    website_url = settings.BASE_URL

    context = {
        "old_email": old_email,
        "new_email": new_email,
        "profile": profile,
        "user": user,
        "company_email": from_email,
        "website_url": website_url,
    }

    notification_subject = render_to_string(
        "profiles/notification_emails/notification_subject.txt",
        context
    ).strip()

    notification_body = render_to_string(
        "profiles/notification_emails/notification_body.txt",
        context
    )

    # Send to old email
    send_mail(
        subject=notification_subject,
        message=notification_body,
        from_email=from_email,
        recipient_list=[old_email],
        fail_silently=True,
    )

    # Send to new email
    send_mail(
        subject=notification_subject,
        message=notification_body,
        from_email=from_email,
        recipient_list=[new_email],
        fail_silently=True,
    )


@login_required
def profile(request):
    """
    Display the user profile, order history,
    and tutorials according to video unlock status.
    """

    profile = get_object_or_404(UserProfile, user=request.user)
    orders = profile.orders.all().order_by("-date")

    context = {
        "profile": profile,
        "user": request.user,
        "on_profile_page": True,
        "orders": orders,
    }
    template = "profiles/profile.html"

    return render(request, template, context)


@login_required
def update_profile(request):
    """
    Handle the profile update form.
    Related to models profile.UserProfile, and
    auth.User, and
    auth.EmailAddress.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(
            request.POST, instance=profile, user=request.user
        )
        if form.is_valid():
            form.save()

            # Compare new email address with allauth User model
            new_email = form.cleaned_data["email"]
            old_email = request.user.email
            if new_email != old_email:
                # Update User model email
                request.user.email = new_email
                request.user.save()

                # Update allauth User model and EmailAddress model
                EmailAddress.objects.filter(
                    user=request.user, primary=True
                ).update(email=new_email)

                # Send notification emails
                send_notification(old_email, new_email, request.user, profile)

            messages.success(request, "Profile updated successfully")
            return redirect(reverse("profile"))
        else:
            # If the form is not valid, restore current user email.
            if "email" in form.errors:
                form.fields["email"].initial = request.user.email
            messages.error(
                request, "Update failed. Please ensure the form is valid."
            )
    else:
        form = UserProfileForm(instance=profile, user=request.user)

    context = {
        "form": form,
        "profile": profile,
        "user": request.user,
    }
    template = "profiles/update_profile.html"

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
