from django import forms

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
        fields = ["name", "email"]
        placeholders = {
            "name": "First Name",
            "email": "Email",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Your First Name",
            "email": "Your Email Address",
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
