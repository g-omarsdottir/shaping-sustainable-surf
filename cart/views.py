from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """
    A view that renders the cart contents page
    Context to avoid duplicate display of cart and cart preview
    """

    context = {
        'is_cart_page': True,
    }

    return render(request, "cart/cart.html", context)


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
    print(request.session["cart"])
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
