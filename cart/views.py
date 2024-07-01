from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import DiscountCode
from products.models import Product
from .forms import DiscountCodeForm


def view_cart(request):
    """
    A view that renders the cart contents page
    Context to avoid duplicate display of cart and cart preview
    """

    template = "cart/cart.html"

    discount_form = DiscountCodeForm()

    if request.method == 'POST':
        discount_form = DiscountCodeForm(request.POST)
        if discount_form.is_valid():
            discount = discount_form.cleaned_data['code']
            if discount:
                request.session['discount_code'] = discount.code
                messages.success(
                        request, f"Discount code '{discount.code}' applied. "
                        f"Amount: €{discount.amount}"
                    )
            else:
                request.session.pop('discount_code', None)
                messages.error(request, "Invalid or inactive discount code.")
        return redirect('view_cart')

    context = {
    "is_cart_page": True,
    "discount_form": discount_form,
    }

    return render(request, template, context)


def add_to_cart(request, item_id):
    """
    Add a product to the shopping cart
    """

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get("redirect_url")

    cart = request.session.get("cart", {})

    if item_id in cart:
        messages.info(request, f"{product.name} is already in your cart")
    else:
        cart[item_id] = 1
        messages.success(request, f"Added {product.name} to your cart")

    request.session["cart"] = cart
    return redirect(redirect_url)


def remove_from_cart(request, item_id):
    """
    Remove the item from the shopping cart
    """

    try:
        product = get_object_or_404(Product, pk=item_id)
        cart = request.session.get("cart", {})

        if str(item_id) in cart:
            del cart[str(item_id)]
            request.session["cart"] = cart
            messages.success(request, f"Removed {product.name} from your cart")
        else:
            messages.error(request, "This item was not in your cart")

    except Exception as e:
        messages.error(request, f"Error removing item: {e}")

    return redirect('view_cart')
