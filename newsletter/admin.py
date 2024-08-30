from django.contrib import admin

from .models import Subscriber

@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):

    fields = (
        "email",
        "accepted_terms",
        "unsubscribe_token",
    )

    list_display = (
            "email",
        )

    search_fields = (
        "email",
    )
