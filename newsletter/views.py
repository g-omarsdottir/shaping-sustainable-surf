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


def get_newsletter_discount_code():
    """
    Get newsletter discount code.
    Discount code is stored in :model:`cart.DiscountCode`.
    Returns:
        DiscountCode: DiscountCode object
    """
    return DiscountCode.objects.filter(
        code="ALOHA-WELCOME", active="Yes"
    ).first()


def generate_unsubscribe_url(subscriber):
    """
    Generate unsubscribe URL for each subscriber.
    Unique URL created from unique unsubscribe token and base url
        to avoid malicious unsubscriptions.
    Args:
        subscriber (Subscriber): unsubscribe_token
    Returns:
        str: unsubscribe URL
    """
    token = subscriber.unsubscribe_token
    relative_url = reverse("unsubscribe", args=[token])
    return f"{settings.BASE_URL}{relative_url}"


def send_subscribe_confirmation(subscriber):
    """
    Send confirmation email to a new newsletter subscriber.
    Includes unsubscribe URL and newsletter discount code.
    Args:
        subscriber (Subscriber): Subscriber
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
    Upon successful subscription,
        - trigger creation of unsubscribe token in
            save method of :model:`newsletter.Subscriber`,
        - trigger sending a confirmation email including
            unsubscribe URL and newsletter discount code, and
        - display a success page including newsletter discount code.
    Args:
        request (HttpRequest): request object
    Returns:
        HttpResponse: redirect to success page (POST), or
        HttpResponse: render subscribe page (GET)
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
    Process unsubscription requests using the unique token, which is
        - generated in save method of :model:`newsletter.Subscriber`, and
        - triggered in subscribe().
    Upon successful unsubscription, deletes the subscriber from the database.
    Args:
        token (str): The unique unsubscribe token.
    Returns:
        HttpResponse: The rendered unsubscribe confirmation page.
    """
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

    return render(request, template)
