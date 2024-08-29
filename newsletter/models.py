from django.db import models
import secrets


class Subscriber(models.Model):
    """
    Model for newsletter subscription.
    Generate a secure token for unsubscribe link
    for each subscriber to unsubscribe from newsletter.
    """
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False
    )
    date_added = models.DateTimeField(auto_now_add=True)
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
