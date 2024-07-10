from django.contrib import admin
from django.utils.html import strip_tags
from django_summernote.admin import SummernoteModelAdmin

from .models import Product, Category, Subcategory


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Fields to display and search by in admin panel.
    Summernote for user-friendly rich-text editor.
    """

    summernote_fields = ("description",)

    list_display = (
        "name",
        "category",
        "subcategory",
        "price",
        "short_description",
        "image",
        "video_url",
        "status",
    )
    list_filter = (
        "category",
        "subcategory",
        "status",
    )
    search_fields = (
        "name",
        "description",
    )

    def short_description(self, obj):
        """
        Return a shortened version of the description.
        """
        # Strip HTML tags and truncate to 50 characters
        clean_description = strip_tags(obj.description)
        return (clean_description[:47] + "...") if len(clean_description) > 50 else clean_description

    short_description.short_description = "Description"


admin.site.register(Category)
admin.site.register(Subcategory)
