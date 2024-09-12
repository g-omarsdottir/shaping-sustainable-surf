from django import forms
from django.utils.safestring import mark_safe

from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    """
    Form to subscribe to newsletter.
    Related to :model:`newsletter.Subscriber`.
    ***Template:***
    :template:`newsletter/subscribe.html`
    """

    class Meta:
        """
        Define form fields for Subscriber model.
        """
        model = Subscriber
        fields = ["email", "accepted_terms"]

        # Add placeholder and id for JavaScript client-side validation
        widgets = {
            "email": forms.EmailInput(attrs={
                "placeholder": "Your Email Address",
                "id": "id_email",
                "autofocus": True,
            }),
            "accepted_terms": forms.CheckboxInput(attrs={
                "id": "id_accepted_terms",
            }),
        }

        # Add custom label for accepted_terms
        labels = {
            "accepted_terms": mark_safe(
                "Yes, send me newsletter emails! "
                "I understand my data will be stored until I unsubscribe. <br>"
                "Check out our "
                "<a href='#' data-toggle='modal' "
                "data-target='#disclaimerModal'>"
                "Disclaimer</a> and <a href='#' "
                "data-toggle='modal' data-target='#privacyPolicyModal'>"
                "Privacy Policy</a> for more information."
            )
        }

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if email:
            email = email.lower().strip()
            if Subscriber.objects.filter(email=email).exists():
                raise forms.ValidationError("You are already subscribed!")
        return email

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        accepted_terms = cleaned_data.get("accepted_terms")
        if email and not accepted_terms:
            raise forms.ValidationError(
                "You must accept the terms to subscribe."
            )
        return cleaned_data
