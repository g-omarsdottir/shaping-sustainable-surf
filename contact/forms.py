from django import forms
from .models import Order

from products.models import Product, Category
from profiles.models import UserProfile

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            "name", "email", "phone", "subject", "message",
            "product", "category", "board_type", "tail", "body_height",
            "body_weight", "board_length", "board_volume", "skill_level",
            "surf_style", "wave_size", "wave_power", "color_theme", "art",
            "remarks"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Define placeholders
        placeholders = {
            "name": "Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "subject": "Subject",
            "message": "Message",
            "category": "Concerning Product",
            "product": "Concerning a Specific Product",
            "board_type": "Board Type",
            "tail": "Tail Type",
            "body_height": "Your Body Height",
            "body_weight": "Your Body Weight",
            "board_length": "Board Length",
            "board_volume": "Board Volume",
            "skill_level": "Your Skill Level",
            "surf_style": "Your Surf Style",
            "wave_size": "Wave Size",
            "wave_power": "Wave Power",
            "color_theme": "Color Theme",
            "art": "Decorative Art",
            "remarks": "Remarks",
        }

        # Set autofocus and required fields
        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            # self.fields[field].label = False

        # Make name and email fields required
        self.fields["name"].required = True
        self.fields["email"].required = True
