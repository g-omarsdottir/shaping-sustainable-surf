import uuid
from django.db import models
from products.models import Product

from django_countries.fields import CountryField


# Create your models here.
class DiscountCode (models.Model):
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

    code = models.CharField(max_length=20, unique=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.CharField(
        max_length=3, choices=ACTIVE_CHOICES, default="Yes"
    )

    def __str__(self):
        return self.code


class Order(models.Model):
    """
    Stores order information.
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    discount_code = models.ForeignKey(
        DiscountCode, on_delete=models.SET_NULL, null=True, blank=True
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    original_cart = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default=""
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    
    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Calculate the total amount with discount code.
        """
        self.order_total = sum(item.product.price for item in self.items.all())
        if self.discount_code:
            self.grand_total = self.order_total - self.discount_code.amount
        else:
            self.grand_total = self.order_total
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it has not been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    """
    A model to associate products with orders.
    """
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name} on order {self.order.order_number}"
