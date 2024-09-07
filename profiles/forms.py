from django import forms
from django.contrib.auth.models import User
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    Form for users to update their profile information.
    Related to :model:`profiles.UserProfile`, and
    :model:`auth.User`.
    ***Template:***
    :template:`profiles/update_profile.html`
    """
    email = forms.EmailField(
        max_length=254, required=True,
        widget=forms.EmailInput(attrs={"id": "id_email"})
    )

    default_postcode = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"id": "id_default_postcode"})
    )

    class Meta:
        """
        Define form fields for UserProfile model.
        auth.User model email field is handled seperately.
        """
        model = UserProfile
        fields = [
            "default_full_name", "default_phone_number",
            "default_street_address1", "default_street_address2",
            "default_town_or_city", "default_postcode",
            "default_county", "default_country",
        ]

    def __init__(self, *args, **kwargs):
        """
        Access the allauth User object to update email field.
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field.
        """
        self.user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        if self.user:
            self.fields["email"].initial = self.user.email

        field_order = [
            "default_full_name", "email", "default_phone_number",
            "default_street_address1", "default_street_address2",
            "default_town_or_city", "default_postcode",
            "default_county", "default_country",
        ]

        # Reorder the fields
        self.fields = {k: self.fields[k] for k in field_order}

        placeholders = {
            "default_full_name": "Name",
            "email": "Email Address",
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
        }

        self.fields["default_full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            class_string = "border-black rounded-0 profile-form-input"
            self.fields[field].widget.attrs["class"] = class_string
            self.fields[field].label = False

        self.fields["default_postcode"].widget.attrs.update({
            "pattern": "[0-9]*",
            "inputmode": "numeric"
        })

    def clean_email(self):
        """
        Validate if the email already exists in the database.
        """
        email = self.cleaned_data.get("email")

        # If email field is empty, return the current email address.
        if not email:
            raise forms.ValidationError(
                f"Email field cannot be empty. "
                "Your current email has been restored."
            )

        if email and email != self.user.email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError(
                    "A user with that email already exists."
                )
        return email

    def save(self, commit=True):
        """
        Override save method to update Allauth User models.
        """
        profile = super().save(commit=False)
        if commit:
            profile.save()
            # Update the user email
            user = profile.user
            user.email = self.cleaned_data["email"]
            user.save()
        return profile
