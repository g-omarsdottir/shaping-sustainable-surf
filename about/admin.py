from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django.utils.html import strip_tags
from .models import AboutUs, FAQ, CustomSurfboard, Resource


@admin.register(AboutUs)
class AboutUsAdmin(SummernoteModelAdmin):
    """
    Admin page for AboutUs model.
    Content field is a Summernote rich text editor field.
    """

    summernote_fields = ("content",)
    list_display = ("title", "custom_content_preview", "image")

    def custom_content_preview(self, obj):
        """
        Returns a shortened human-readable preview of the content field.
        """
        # Strip HTML tags for a plain text preview
        from django.utils.html import strip_tags
        plain_text = strip_tags(obj.content)
        return (plain_text[:50] + "...") if len(plain_text) > 50 else plain_text
    custom_content_preview.short_description = "Content Preview"


@admin.register(FAQ)
class FAQAdmin(SummernoteModelAdmin):
    """
    Admin page for FAQ model.
    Question and Answer fields are a Summernote rich text editor field.
    The order field allows for a convenient manual sorting of the entries.
    """

    summernote_fields = ("answer",)
    list_display = (
        "display_question",
        "display_answer",
        "created_at",
        "order"
    )
    list_editable = ("order",)
    ordering = ("order", "-created_at")
    search_fields = ("question", "answer")

    def display_question(self, obj):
        if len(obj.question) > 50:
            return obj.question[:50] + "..."
        return obj.question
    display_question.short_description = "Question"

    def display_answer(self, obj):
        stripped_answer = strip_tags(obj.answer)
        if len(stripped_answer) > 50:
            return stripped_answer[:50] + "..."
        return stripped_answer
    display_answer.short_description = "Answer"


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

    list_display = ("name", "order")
    search_fields = ("name", "url")
    list_editable = ("order",)
    ordering = ("order",)
