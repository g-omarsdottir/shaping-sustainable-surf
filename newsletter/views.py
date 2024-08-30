import secrets
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings

from .models import Subscriber
from .forms import SubscriberForm
from cart.models import DiscountCode


def subscribe(request):
    """
    View to subscribe to newsletter.
    Unsubscribe token is generated
    in save method of :model:`newsletter.Subscriber`.
    """
    company_email = settings.DEFAULT_FROM_EMAIL

    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            # Trigger save method, create subscriber and unsubscribe token
            subscriber = form.save()
            messages.success(
                request, "You have been subscribed to the newsletter!"
            )
            # Get newsletter discount code
            newsletter_code = DiscountCode.objects.filter(
                code="ALOHA&WELCOME", active="Yes"
            ).first()
            context = {
                    "newsletter_code": newsletter_code,
                    "company_email": company_email,
                }
            if not newsletter_code:
                messages.warning(
                    request,
                    f"Oops! Something went wrong "
                    f"while getting your discount code. "
                    f"Please contact us and we will make it up to you!"
                )
            template = "newsletter/subscribe_success.html"
            return render(request, template, context)
        else:
            messages.error(
                request, "Please check your input and try again."
            )
    else:
        form = SubscriberForm()

    context = {
        "form": form,
        "company_email": company_email,
    }
    template = "newsletter/subscribe.html"

    return render(request, template, context)
