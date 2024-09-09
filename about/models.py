from django.db import models
from django.core.validators import URLValidator

from django.utils.html import strip_tags
from django_resized import ResizedImageField
from autoslug import AutoSlugField


class AboutUs(models.Model):
    """
    Stores the content of about us page.
    """

    title = models.CharField(max_length=200)
    content = models.TextField(max_length=10000)
    image = ResizedImageField(
        size=[400, None],
        upload_to="sss-about/",
        quality=75,
        force_format="webp",
        null=True, blank=True
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "About Us"


class FAQ(models.Model):
    """
    Model to store the FAQ entries.
    """

    question = models.CharField(max_length=1000, verbose_name="Question")
    answer = models.TextField(max_length=5000, verbose_name="Answer")
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        """
        Orders the entries by date or manually.
        """

        ordering = ["order", "-created_at"]
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        """
        Returns the first 50 characters of the question in the admin panel.
        """
        return strip_tags(self.question)[:50]

    def save(self, *args, **kwargs):
        """
        Removes empty spaces from begin and end of Q and A fields.
        Orders the entries if not set manually.
        """
        self.question = strip_tags(self.question.strip())
        self.answer = self.answer.strip()
        if not self.order:
            last_item = FAQ.objects.order_by("-order").first()
            self.order = last_item.order + 1 if last_item else 1
        super().save(*args, **kwargs)


class CustomSurfboard(models.Model):
    """
    Model to store custom surfboards.
    """

    name = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(max_length=1000, null=True, blank=True)
    image = ResizedImageField(
        size=[400, None],
        upload_to="sss-custom_surfboards/",
        quality=75,
        force_format="webp",
        null=True, blank=False
    )
    created_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(
        populate_from="name", always_update=True, unique=True
    )

    class Meta:
        """
        Orders the entries in chronological order, newest first.
        """
        verbose_name = "Custom Surfboard"
        verbose_name_plural = "Custom Surfboards"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Resource(models.Model):
    """
    Model to store the resources.
    Description field is to improve SEO.
    Length is limited to hold mainly long-tail key words.
    """
    name = models.CharField(max_length=200, null=False, blank=False)
    image = ResizedImageField(
        size=[400, None],
        upload_to="sss-resources/",
        quality=75,
        force_format="webp",
        null=True, blank=True
    )
    description = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, validators=[URLValidator()])
    order = models.IntegerField(default=0)

    class Meta:
        """
        Orders the entries manually.
        """
        ordering = ["order"]
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    def __str__(self):
        return self.name
