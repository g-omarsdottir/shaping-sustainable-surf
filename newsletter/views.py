import secrets
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Subscriber
from .forms import SubscriberForm


def subscribe(request):
    """
    View to subscribe to newsletter.
    Unsubscribe token is generated
    in save method of :model:`newsletter.Subscriber`.
    """
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]
            if not Subscriber.objects.filter(email=email).exists():
                subscriber = Subscriber(email=email, name=name)
                # Trigger save method and generate unsubscribe token
                subscriber.save()
                messages.success(
                    request, "You have been subscribed to the newsletter!"
                )
            else:
                messages.info(request, "You are already subscribed!")

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = SubscriberForm()

    context = {
        "form": form,
    }
    template = "newsletter/subscribe.html"

    return render(request, template, context)
