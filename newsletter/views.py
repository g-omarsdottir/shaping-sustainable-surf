import secrets
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Subscriber, Newsletter
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


def send_newsletter(request, newsletter_id):
    """
    View to send a newsletter to all subscribers.
    Handle calls from
        - the admin interface (with a request object), and
        - from the signal in signals.py
            (without a request object) for front-end functionality (tbd).
    Args:
        request (HttpRequest): request object
        newsletter_id (int): The ID of the newsletter to send.
    Returns:
        HttpResponse: upon successful sending conditional redirect to
        - list of newsletters in admin panel if request comes from admin, or
        - current path for front-end functionality (tbd).
    """
    newsletter = get_object_or_404(Newsletter, id=newsletter_id)
    subscribers = Subscriber.objects.all()
    from_email = settings.DEFAULT_FROM_EMAIL
    website_url = settings.BASE_URL

    # Check the status of the newsletter
    if newsletter.status == "draft":
        if request:
            messages.error(
                request, "You cannot send a draft. Check the 'Status' field.",
                extra_tags="safe"
            )
        return False

    if newsletter.sent_date:
        if request:
            messages.warning(
                request, "This newsletter has already been sent.",
                extra_tags="safe"
            )
            return False

    if not subscribers.exists():
        if request:
            messages.warning(
                request, "No subscribers to send the newsletter to.",
                extra_tags="safe"
            )
            return False

    # Render newsletter subject (not personalized)
    newsletter_subject = render_to_string(
        "newsletter/emails/newsletter_subject.txt",
        {"newsletter": newsletter}
        ).strip()

    try:
        # Add personalized content for each subscriber
        for subscriber in subscribers:
            # Generate the personalized unsubscribe URL for each subscriber
            unsubscribe_url = generate_unsubscribe_url(subscriber)

            # Render personalized newsletter body
            personalized_body = render_to_string(
                "newsletter/emails/newsletter_body.txt",
                {
                        "newsletter": newsletter,  # The newsletter object
                        "subscriber": subscriber,
                        "company_email": from_email,
                        "website_url": website_url,
                        "unsubscribe_url": unsubscribe_url,
                }
            )
            send_mail(
                newsletter_subject,
                message=personalized_body,
                from_email=from_email,
                recipient_list=[subscriber.email],
            )

        newsletter.sent_date = timezone.now()
        newsletter.status = "done"
        newsletter.save()

        if request:
            messages.success(
                request, "Newsletter sent successfully!",
                extra_tags="safe"
            )

        return True

    except Exception as e:
        if request:
            messages.error(
                request, f"Failed to send newsletter: {str(e)}",
                extra_tags="safe"
            )
        return False

    # Conditional redirect
    if request:
        if request.path.startswith("/admin/"):
            return redirect("admin:newsletter_newsletter_changelist")
        else:
            return redirect(request.path)
    else:
        return
