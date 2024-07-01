from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm, DiscountCodeForm
from .models import Order, OrderItem, DiscountCode
from products.models import Product
from cart.contexts import cart_contents

def checkout(request):

    template = "checkout/checkout.html"

    cart = request.session.get("cart", {})
    if not cart:
        messages.error(
            request, "There's nothing in your cart at the moment"
        )
        return redirect(reverse("tutorials"))

    order_form = OrderForm()
    discount_form = DiscountCodeForm()
    current_cart = cart_contents(request)
    # Initial grand_total from cart before order is created
    total = current_cart['total']


    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        discount_form = DiscountCodeForm(request.POST)

        if order_form.is_valid() and discount_form.is_valid():
            order = order_form.save(commit=False)

            # Apply discount if discount code valid
            discount_code = discount_form.cleaned_data['code']
            if discount_code:
                try:
                    discount = DiscountCode.objects.get(code=discount_code, active="Yes")
                    order.discount_code = discount
                    messages.success(
                        request, f"Discount code '{discount.code}' applied. "
                        f"Amount: €{discount.amount}"
                    )
                except DiscountCode.DoesNotExist:
                    messages.error(request, "Invalid or inactive discount code.")
                    order.discount_code = None
            else:
                order.discount_code = None

            order.save()
            # Update order totals. Refers to method defined in Order model
            order.update_total()
            grand_total = order.grand_total
            # Process payment and complete order
            # Create order items
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                order_item = OrderItem(
                    order=order,
                    product=product,
                )
                order_item.save()

                # Calculate final total
                order.update_total()

                # Clear the cart
                del request.session['cart']

        # Redirect to a success page
        return redirect('checkout_success', order_number=order.order_number)

    else:
        messages.error(
            request, "There was an error with your form. "
            "Please double check your information."
        )

    context = {
        "order_form": order_form,
        "discount_form": discount_form,
        "cart_items": current_cart['cart_items'],
        "total": total,
        "order_total": total,  # Variable cart's total
        "product_count": current_cart['product_count'],
        "grand_total": total,  # Initially, grand_total is the same as total
    }

    return render(request, template, context)
