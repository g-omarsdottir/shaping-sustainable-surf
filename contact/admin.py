from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Fields to display in admin panel.
    """

    list_display = (
        "user_profile",
        "name",
        "subject",
        "category",
        "email",
        "sent_at",
        "message_read"
    )

    list_filter = ("message_read",)

    fields = (
        "sent_at",
        "message_read",
        "user_profile",
        "name",
        "email",
        "phone",
        "subject",
        "message",
        "category",
        "board_type",
        "tail",
        "body_height",
        "body_weight",
        "board_length",
        "board_volume",
        "skill_level",
        "surf_style",
        "wave_size",
        "wave_power",
        "color_theme",
        "art",
        "remarks",
    )
