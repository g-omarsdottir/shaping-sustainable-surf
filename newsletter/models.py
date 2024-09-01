from django.db import models
import secrets


class Subscriber(models.Model):
    """
    Model for newsletter subscription.
    Generate a secure token for unsubscribe link
    for each subscriber to unsubscribe from newsletter.
    """
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False
    )
    date_added = models.DateTimeField(auto_now_add=True)
    accepted_terms = models.BooleanField(
        default=False, null=False, blank=False
    )
    unsubscribe_token = models.CharField(max_length=64, unique=True)

    def save(self, *args, **kwargs):
        """
        Generate a secure unsubscribe token.
        Save method triggered in view at form submission.
        """
        if not self.unsubscribe_token:
            self.unsubscribe_token = secrets.token_urlsafe(48)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    """
    Model for the newsletter.
    """
    STATUS = [
        ("draft", "Save as Draft"),
        ("finalized", "Save as Finalized Version"),
        ("send", "Save and Send Newsletter Now"),
        ("done", "Done and Sent"),
    ]
    subject = models.CharField(max_length=254, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=20, choices=STATUS, default="Draft")
    created_date = models.DateTimeField(auto_now_add=True)
    sent_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject
