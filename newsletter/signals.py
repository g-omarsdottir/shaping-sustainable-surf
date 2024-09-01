from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Newsletter


@receiver(post_save, sender=Newsletter)
def send_newsletter_if_status_is_send(sender, instance, **kwargs):
    """
    Send newsletter if status is "send".
    """
    if instance.status == "send":
        from .views import send_newsletter
        send_newsletter(None, instance.id)
