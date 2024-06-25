from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from djrichtextfield.models import RichTextField

class Category(models.Model):
    """
    Stores main category for product.
    Related to :model:`Product`
    """

    CATEGORIES = [
        ("Tutorial", "Tutorial"),
        ("Surfboard", "Surfboard"),
    ]

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=20, choices=CATEGORIES)

    def __str__(self):
        return (
            self.get_name_display()
        )  # get_name_display returns "human-readable" value


class Subcategory(models.Model):
    """
    Stores subcategory for product.
    Related to :model:`Product`
    """

    SUBCATEGORIES = [
        ("Shaping", "Shaping"),
        ("Materials", "Materials & Tools"),
        ("Surfing", "Surfing"),
    ]

    class Meta:
        verbose_name_plural = "Subcategories"

    name = models.CharField(max_length=50, choices=SUBCATEGORIES)

    def __str__(self):
        return (
            self.get_name_display()
        )  # get_name_display returns "human-readable" value


class Product(models.Model):
    """
    Stores products.
    Related to :model:`Category`
    and :model:`Subcategory`
    and :model:`Review`
    """

    STATUS = [
        ("Draft", "Draft"),
        ("Publish", "Publish"),
    ]

    name = models.CharField(max_length=254)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=False
    )
    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.SET_NULL, null=True, blank=False
    )
    price = models.DecimalField(
        max_digits=6, null=True, blank=False, decimal_places=2
    )
    description = RichTextField(max_length=3000, null=True, blank=False)
    image = ResizedImageField(
        size=[400, None],
        upload_to="sss_products/",
        null=True,
        blank=True,
        quality=75,
        force_format="webp",
    )
    video_url = models.URLField(max_length=254, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True
    )
    status = models.CharField(max_length=20, choices=STATUS, default="Draft")

    def __str__(self):
        return self.name
