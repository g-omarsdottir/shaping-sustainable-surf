from django import forms
from .models import Contact

from products.models import Category


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ["user_profile"]

        fields = [
            "name", "email", "phone", "subject", "message",
            "category", "board_type", "tail", "body_height",
            "body_weight", "board_length", "board_volume", "skill_level",
            "surf_style", "wave_size", "wave_power", "color_theme", "art",
            "remarks"
        ]

    def __init__(self, *args, **kwargs):
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

        # Set autofocus and required fields
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field in placeholders:
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False

        # Make name and email fields required
        self.fields["name"].required = True
        self.fields["email"].required = True

        # Set initial values for other fields
        for field, value in initial_data.items():
            if field in self.fields:
                self.fields[field].initial = value
