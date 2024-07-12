from django import forms
from .models import Contact

from products.models import Category


class ContactForm(forms.ModelForm):
    """
    Contact form to collect user data for contact.
    Utilizes TextInput widget for Integer fields to allow numeric input,
        while avoiding the browser's default numeric keyboard
        with arrow keys (up and down) for simpler user interface.
    """

    board_length = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "pattern": "[0-9]*",
                "inputmode": "numeric"
            }
        ),
        required=False,
    )
    board_volume = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "pattern": "[0-9]*",
                "inputmode": "numeric"
            }
        ),
        required=False,
    )
    body_height = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "pattern": "[0-9]*",
                "inputmode": "numeric"
            }
        ),
        required=False,
    )
    body_weight = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "pattern": "[0-9]*",
                "inputmode": "numeric"
            }
        ),
        required=False,
    )

    class Meta:
        """

        """

        model = Contact
        exclude = ["user_profile"]

        fields = [
            "name",
            "email",
            "phone",
            "subject",
            "message",
            "category",
            "board_type",
            "tail",
            "body_height",
            "body_weight",
            "board_length",
            "board_volume",
            "skill_level",
            "surf_style",
            "wave_size",
            "wave_power",
            "color_theme",
            "art",
            "remarks",
        ]

    def clean(self):
        cleaned_data = super().clean()
        integer_fields = [
            "board_length",
            "board_volume",
            "body_height",
            "body_weight"
        ]

        for field in integer_fields:
            value = cleaned_data.get(field)
            if value is not None:
                try:
                    int(value)
                except ValueError:
                    self.add_error(
                        field, "Please enter only whole numbers."
                    )
        return cleaned_data

    def clean_message(self):
        """
        Clean message field to avoid empty messages.
        """

        message = self.cleaned_data.get("message")
        if message:
            message = message.strip()
            if not message:
                raise forms.ValidationError("Message field cannot be empty.")
        return message

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email address is required.")
        return email

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
            labels and set autofocus on first field.
        """

        initial_data = kwargs.pop("initial_data", {})
        super().__init__(*args, **kwargs)

        # Define placeholders
        placeholders = {
            "name": "Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "subject": "Subject",
            "message": "Message",
            "category": "Category",
            "board_type": "Board Type",
            "tail": "Tail Type",
            "board_length": "Board Length",
            "board_volume": "Board Volume",
            "body_height": "Your Body Height",
            "body_weight": "Your Body Weight",
            "skill_level": "Your Skill Level",
            "surf_style": "Your Surf Style",
            "wave_size": "Wave Size",
            "wave_power": "Wave Power",
            "color_theme": "Color Theme",
            "art": "Decorative Art",
            "remarks": "Further Remarks",
        }

        # Make name and email fields required
        self.fields["name"].required = True
        self.fields["email"].required = True

        # Set autofocus and required fields
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field in placeholders:
                if not isinstance(self.fields[field], forms.ChoiceField):
                    placeholder = placeholders[field]
                    if self.fields[field].required:
                        placeholder += " *"
                    else:
                        placeholder = placeholders[field]
                    self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"

        # Set initial values for other fields
        for field, value in initial_data.items():
            if field in self.fields:
                self.fields[field].initial = value
