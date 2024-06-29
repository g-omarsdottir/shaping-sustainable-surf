from django.contrib import admin
from .models import DiscountCode


# Register your models here.
@admin.register(DiscountCode)
class DiscountCodeAdmin(admin.ModelAdmin):
    """
    Fields to display and search by in admin panel.
    """

    list_display = ("code", "amount", "active")
    list_filter = ("active",)
    search_fields = ("code", "code")
    ordering = ("-active", "code")
    actions = ["activate_codes", "deactivate_codes"]

    def activate_codes(self, request, queryset):
        queryset.update(active="Yes")
    activate_codes.short_description = "Mark selected codes as active"

    def deactivate_codes(self, request, queryset):
        queryset.update(active="No")
    deactivate_codes.short_description = "Mark selected codes as inactive"
