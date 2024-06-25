from django.contrib import admin
from .models import Product, Category, Subcategory

# Models


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Fields to display and search by in admin panel.
    # Summernote for user-friendly rich-text editor. ###
    """

    list_display = ("name", "category", "subcategory", "price", "description", "image", "video_url", "status",)
    list_filter = ("status", "category", "subcategory")
    search_fields = ("name", "description")
    actions = ["publish_products", "unpublish_products"]

    def publish_products(self, request, queryset):
        queryset.update(status=1)

    publish_products.short_description = "Publish product"

    def unpublish_products(self, request, queryset):
        queryset.update(status=0)

    unpublish_products.short_description = "Save as draft"


admin.site.register(Category)
admin.site.register(Subcategory)
