from django.db import models


# Create your models here.
class DiscountCode(models.Model):
    """
    Stores discount codes and their values.
    """

    class Meta:
        """
        Verbose name and plural name for admin panel.
        """
        verbose_name = "Discount Codes"
        verbose_name_plural = "Discount Codes"

    ACTIVE_CHOICES = [
        ("Yes", "Yes"),
        ("No", "No"),
    ]

    code = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.CharField(
        max_length=3, choices=ACTIVE_CHOICES, default="Yes"
    )

    def __str__(self):
        return self.code
