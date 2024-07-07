from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product, Category, Subcategory

# Models


@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    """
    Fields to display and search by in admin panel.
    # Summernote for user-friendly rich-text editor. ###
    """

    summernote_fields = ("description",)

    list_display = (
        "name",
        "category",
        "subcategory",
        "price",
        "description",
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

admin.site.register(Category)
admin.site.register(Subcategory)
