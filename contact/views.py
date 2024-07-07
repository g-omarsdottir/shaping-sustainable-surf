from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse

from .models import Contact
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):

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
            return redirect(reverse(
                "contact_success", args=[contact.pk])
            )
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
                "user_profile": user_profile,
                "name": user_profile.user.get_full_name() or user_profile.user.username,
                "email": user_profile.user.email,
                "phone": user_profile.default_phone_number if hasattr(user_profile, "default_phone_number") else "",
                }
        contact_form = ContactForm(initial=initial_data)

    template = "contact/contact.html"

    context = {
        "contact_form": contact_form,
    }

    return render(request, template, context)


def contact_success(request, contact_id):
    
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
