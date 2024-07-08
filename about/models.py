from django.db import models
from django.core.validators import URLValidator

from django_resized import ResizedImageField
from autoslug import AutoSlugField


class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = ResizedImageField(
        upload_to="sss-about/", null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.question

    class Meta:
        ordering = ["order"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class CustomSurfboard(models.Model):
    """
    Model to store custom surfboards.
    """

    class Meta:
        """
        Orders the entries in chronological order, newest first.
        """
        verbose_name = "Custom Surfboard"
        verbose_name_plural = "Custom Surfboards"
        ordering = ["-created_at"]

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=500, null=True, blank=True)
    image = ResizedImageField(upload_to="sss-custom_surfboards/")
    created_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(
        populate_from="name", always_update=True, unique=True
    )

    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=500, validators=[URLValidator()])
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.name
