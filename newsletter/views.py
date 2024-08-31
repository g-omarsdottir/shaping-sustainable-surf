import secrets
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Subscriber
from .forms import SubscriberForm
from cart.models import DiscountCode

import logging

logger = logging.getLogger(__name__)


def get_newsletter_discount_code():
    """
    Get newsletter discount code.
    Discount code is stored in :model:`cart.DiscountCode`.
    """
    return DiscountCode.objects.filter(
        code="ALOHA-WELCOME", active="Yes"
    ).first()


def generate_unsubscribe_url(subscriber):
    """
    Generate unsubscribe URL for the subscriber.
    """
    token = subscriber.unsubscribe_token
    relative_url = reverse("unsubscribe", args=[token])
    return f"{settings.BASE_URL}{relative_url}"


def send_subscribe_confirmation(subscriber):
    """
    Send newsletter subscription confirmation email to the subscriber.
    """
    from_email = settings.DEFAULT_FROM_EMAIL
    # Get unsubscribe URL
    unsubscribe_url = generate_unsubscribe_url(subscriber)
    # Get newsletter discount code
    newsletter_code = get_newsletter_discount_code()
    
    # Email to subscriber
    confirmation_subject = render_to_string(
        "newsletter/emails/subscribe_confirmation_subject.txt",
    )
    confirmation_body = render_to_string(
        "newsletter/emails/subscribe_confirmation_body.txt",
        {
            "subscriber": subscriber,
            "newsletter_code": newsletter_code,
            "company_email": from_email,
            "unsubscribe_url": unsubscribe_url,
        }
    )
    
    send_mail(
        confirmation_subject,
        confirmation_body,
        from_email,
        [subscriber.email]
    )


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
            # Send confirmation email
            send_subscribe_confirmation(subscriber)
            messages.success(
                request, "You have been subscribed to the newsletter!"
            )
            # Get newsletter discount code
            newsletter_code = get_newsletter_discount_code()
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


def unsubscribe(request, token):
    """
    View to unsubscribe from newsletter mailing list.
    Unsubscribe token is generated
        in save method of :model:`newsletter.Subscriber`
        at subscription.
    """
    logger.debug(f"Unsubscribe view called with token: {token}")
    logger.info(f"Received token: {token}")
    print(f"Received token: {token}")
    try:
        subscriber = get_object_or_404(Subscriber, unsubscribe_token=token)
        subscriber.delete()
        messages.success(
            request,
            f"Your email has been unsubscribed and removed from our database."
        )
    except Subscriber.DoesNotExist:
        messages.error(
            request,
            f"Something went wrong. Try again later or contact us for help."
        )

    template = "newsletter/unsubscribe.html"

    print(f"Received token: {token}")

    return render(request, template, {"token": token})
