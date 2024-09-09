from django.contrib import admin

from .models import Subscriber, Newsletter
from .views import send_newsletter


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):

    fields = (
        "email",
        "accepted_terms",
        "unsubscribe_token",
    )

    list_display = (
            "email",
            "date_added",
        )

    search_fields = (
        "email",
    )


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Newsletter model.

    Attributes:
        action: Send newsletter.
        list_display: Fields to display in list view the admin panel.
        list_filter: Fields to use for filtering in the list view.
        actions: Custom action to send newsletter.
    """
    fields = (
        "subject",
        "body",
        "status",
    )

    list_display = (
            "subject",
            "status",
            "created_date",
            "sent_date",
        )

    list_filter = ("status",)

    actions = ["send_selected_newsletter", ]

    def send_selected_newsletter(self, request, queryset):
        for newsletter in queryset:
            if newsletter.status != "send":
                newsletter.status = "send"
                newsletter.save()  # Trigger the signal
            else:
                messages.warning(
                    request,
                    f"Newsletter '{newsletter.subject}' is already "
                    f"set to send.",
                    level="WARNING"
                )
    send_selected_newsletter.short_description = "Send selected newsletter"
