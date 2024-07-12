from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from .models import Contact
from .forms import ContactForm
from profiles.models import UserProfile


def send_contact_email(contact):
    """
    Send contact confirmation email to customer
        and notification email to store owner.
    Email content is rendered from templates in contact/confirmation_emails.
    """

    from_email = settings.DEFAULT_FROM_EMAIL

    # Email to customer
    customer_subject = render_to_string(
        "contact/confirmation_emails/confirmation_email_subject.txt",
         {"contact": contact}
    ).strip()
    customer_body = render_to_string(
        "contact/confirmation_emails/confirmation_email_body.txt",
        {"contact": contact, "company_email": from_email}
    )
    
    send_mail(
        customer_subject,
        customer_body,
        from_email,
        [contact.email]
    )

    # Email to store owner (using DEFAULT_FROM_EMAIL as recipient)
    owner_subject = f"New Contact Message: {contact.subject}"
    owner_body = render_to_string(
        "contact/confirmation_emails/owner_notification_email.txt",
        {"contact": contact}
    )

    send_mail(
        owner_subject,
        owner_body,
        from_email,
        [from_email]
    )


def contact(request):
    """
    Handles the rendering and processing of a contact form.
    Displays a blank or pre-filled form
        with information from UserProfile model.
    Validates the form data,
        associates it with the UserProfile if applicable,
        sends the email notification,
        and redirects the user to a success page.
    """

    company_email = settings.DEFAULT_FROM_EMAIL
    contact_form = ContactForm()
    user_profile = None

    if request.user.is_authenticated:
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            pass

    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            if user_profile:
                contact.user_profile = user_profile
            contact.save()
            try:
                send_contact_email(contact)
                return redirect(reverse(
                    "contact_success", args=[contact.pk])
                )
            except Exception as e:
                messages.error(request, f"An error occurred while sending your message: {str(e)}")
        else:
            messages.error(
                request,
                "There was an error with your form. "
                "Please double check your information.",
            )
    else:
        initial_data = {}
        if user_profile:
            initial_data = {
                "user_profile": user_profile,
                "name": (
                    user_profile.user.get_full_name()
                    or user_profile.user.username
                ),
                "email": user_profile.user.email,
                "phone": user_profile.default_phone_number if hasattr(
                    user_profile, "default_phone_number"
                ) else "",
                }
        contact_form = ContactForm(initial=initial_data)

    template = "contact/contact.html"

    context = {
        "contact_form": contact_form,
        "company_email": company_email,
    }

    return render(request, template, context)


def contact_success(request, contact_id):
    """
    Displays a success message and the contact information.
    Context: contact object to display the submitted form data.
    """

    contact = get_object_or_404(Contact, pk=contact_id)

    success_message = (
        f"Thank you for contacting us, {contact.name}! "
        f"A confirmation email will be sent to {contact.email}."
    )
    messages.success(request, success_message)

    template = "contact/contact_success.html"

    context = {
        "contact": contact,
    }

    return render(request, template, context)
