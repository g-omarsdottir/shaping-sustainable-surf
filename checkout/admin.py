from django.contrib import admin
from .models import Order, OrderItem


# Register your models here.
class OrderItemAdminInline(admin.TabularInline):
    """
    Fields to display order items inline in OrderAdmin interface.
    Settings ensure that the order items are not editable.
    """

    model = OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Fields to display and search orders in admin panel.
    """

    inlines = (OrderItemAdminInline,)

    readonly_fields = (
        "order_number",
        "date",
        "order_total",
        "grand_total",
        "original_cart",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "date",
        "order_total",
        "discount_code",
        "grand_total",
        "original_cart",
        "stripe_pid",
        # "user_profile",
        "full_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "postcode",
        "town_or_city",
        "county",
        "country",
    )

    list_display = (
        "order_number",
        "date",
        "full_name",
        "order_total",
        "discount_code",
        "grand_total",
    )

    ordering = ("-date",)
