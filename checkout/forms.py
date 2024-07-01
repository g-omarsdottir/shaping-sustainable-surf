from django import forms
from .models import Order, DiscountCode


class OrderForm(forms.ModelForm):
    """
    Order form to collect user data for order.
    """

    class Meta:
        """
        Meta class to define fields to be used.
        """

        model = Order

        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "postcode",
            "town_or_city",
            "county",
            "country",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False


class DiscountCodeForm(forms.Form):
    """
    Form to collect and validate discount code.
    """
    code = forms.CharField(max_length=20, required=False)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated labels.
        """
        super().__init__(*args, **kwargs)
        self.fields['code'].widget.attrs.update({
            'placeholder': 'Discount Code',
            'class': 'stripe-style-input'
        })
        self.fields['code'].label = False

    def clean_code(self):
        """
        Returns discount code if it exists and is active.
        """
        code = self.cleaned_data.get('code')
        if code:
            try:
                discount = DiscountCode.objects.get(code=code, active="Yes")
                return discount
            except DiscountCode.DoesNotExist:
                raise forms.ValidationError(
                    "Invalid or inactive discount code."
                )
        return None
