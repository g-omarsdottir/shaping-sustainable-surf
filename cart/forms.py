from django import forms
from .models import DiscountCode


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
        self.fields["code"].widget.attrs.update(
            {"placeholder": "Discount Code", "class": "stripe-style-input"}
        )
        self.fields["code"].label = False

    def clean_code(self):
        """
        Returns discount code if it exists and is active.
        """
        code = self.cleaned_data.get("code")
        if code:
            try:
                discount = DiscountCode.objects.get(code=code, active="Yes")
                return discount
            except DiscountCode.DoesNotExist:
                raise forms.ValidationError(
                    "Invalid or inactive discount code."
                )
        return None
