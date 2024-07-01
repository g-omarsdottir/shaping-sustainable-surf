from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from .forms import OrderForm
from .models import Order, OrderItem
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

    if request.method == 'POST':
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
            
            # Process payment and complete order
            # Create order items
            for item_id, quantity in cart.items():
                product = Product.objects.get(id=item_id)
                order_item = OrderItem(
                    order=order,
                    product=product,
                )
                order_item.save()

            # Redirect to a success page
            return redirect('checkout_success', order_number=order.order_number)
        else:
            messages.error(
                request, "There was an error with your form. "
                "Please double check your information."
            )

    context = {
        "order_form": order_form,
    }

    return render(request, template, context)
