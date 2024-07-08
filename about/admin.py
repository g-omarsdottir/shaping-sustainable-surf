from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import AboutUs, FAQ, CustomSurfboard, Resource


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    """
    Admin page for AboutUs model.
    Content field is a Summernote rich text editor field.
    """

    summernote_fields = ("content",)
    list_display = ("title", "content", "image")


@admin.register(FAQ)
class FAQAdmin(SummernoteModelAdmin):
    """
    Admin page for FAQ model.
    Question and Answer fields are a Summernote rich text editor field.
    The order field allows for a convenient manual sorting of the entries.
    """

    summernote_fields = ("question", "answer")
    list_display = ("question", "answer", "order")
    list_editable = ("order",)
    ordering = ("order",)
    search_fields = ("question", "answer")


@admin.register(CustomSurfboard)
class CustomSurfboardAdmin(admin.ModelAdmin):
    """
    Admin page for CustomSurfboard model.
    """

    list_display = ("name",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)
    search_fields = ("name",)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    """
    Admin page for Resource model.
    The order field allows for a convenient manual sorting of the resources.
    """

    list_display = ("name", "url", "order")
    search_fields = ("name", "url")
    list_editable = ("order",)
    ordering = ("order",)
