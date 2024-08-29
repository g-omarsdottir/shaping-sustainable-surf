from django.contrib import admin

from .models import Subscriber

@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):

    fields = (
        "name",
        "email",
        "unsubscribe_token",
    )

    list_display = (
            "name",
            "email",
        )

    search_fields = (
        "name",
        "email",
    )
