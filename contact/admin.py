from django.contrib import admin
from .models import Contact, Art


@admin.register(Art)
class ArtAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Art model.
    """
    list_display = ("type",)
    ordering = ("type",)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Contact model.

    Attributes:
        action: Mark selected messages as read.
        list_display: Fields to display in the admin panel.
        list_filter: Filter the list of Contact objects.
        search_fields: Fields that can be searched in the admin interface.
        readonly_fields: Fields that cannot be edited in the admin interface.
            For database integrity:
                all fields except for message_read are readonly.
        fields: The order and grouping of fields in the detail view.

    Method:
        mark_as_read: Custom action to mark selected messages as read.
    """

    actions = ["mark_as_read"]

    def mark_as_read(self, request, queryset):
        updated = queryset.update(message_read=True)
        self.message_user(
            request, f"{updated} message(s) have been marked as read.",
            messages.SUCCESS
        )
    mark_as_read.short_description = "Mark selected messages as read"

    list_display = (
        "user_profile",
        "name",
        "subject",
        "category",
        "email",
        "sent_at",
        "message_read",
    )

    list_filter = (
        "message_read",
        "name",
        "category",
    )

    search_fields = (
        "name",
        "email",
        "category__name",
        "user_profile__user__username",
    )

    readonly_fields = [
        "sent_at",
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
    ]

    fields = (
        "message_read",
        "sent_at",
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
