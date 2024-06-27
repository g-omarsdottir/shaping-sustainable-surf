from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_cart(request):
    """
    A view that renders the cart contents page
    """

    return render(request, "cart/cart.html")


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
