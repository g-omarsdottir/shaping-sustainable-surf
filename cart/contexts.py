from django.shortcuts import get_object_or_404
from .models import DiscountCode
from products.models import Product


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get("cart", {})

    for item_id in cart:
        product = get_object_or_404(Product, pk=item_id)
        total += product.price
        product_count += 1
        cart_items.append(
            {
                "item_id": item_id,
                "product": product,
            }
        )

    discount_code = request.session.get("discount_code")
    discount = None
    discount_amount = 0
    grand_total = total

    if discount_code:
        try:
            discount = DiscountCode.objects.get(code=discount_code, active="Yes")
            discount_amount = discount.amount
            # Ensuring grand_total is not negative
            grand_total = max(total - discount_amount, 0)
        except DiscountCode.DoesNotExist:
            # If discount code is invalid, remove from session
            request.session.pop("discount_code", None)

    context = {
        "cart_items": cart_items,
        "total": total,
        "product_count": product_count,
        "discount": discount,
        "discount_amount": discount_amount,
        "grand_total": grand_total,
    }

    return context
