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

    if request.method == "POST":
        discount_form = DiscountCodeForm(request.POST)
        if discount_form.is_valid():
            code = discount_form.cleaned_data["code"]
            try:
                discount = DiscountCode.objects.get(code=code, active="Yes")
                request.session["discount_code"] = discount.code
                messages.success(
                    request,
                    f"Discount code '{discount.code}' applied. "
                    f"Amount: €{discount.amount}",
                )
            except DiscountCode.DoesNotExist:
                request.session.pop("discount_code", None)
        else:
            messages.error(request, "Invalid or inactive discount code.")
        return redirect("view_cart")

    # Retrieves discount code from the session if it exists
    discount_code = request.session.get("discount_code", "")

    context = {
        "is_cart_page": True,
        "discount_form": discount_form,
        "discount_code": discount_code,
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

    return redirect("view_cart")


def remove_discount_code(request):
    """
    Remove the discount code from the shopping cart
    """

    try:
        # Clear the discount_code from the session
        request.session.pop("discount_code", None)
        messages.success(request, "Discount code removed successfully.")
    except KeyError:
        # Handle case where discount_code does not exist in the session
        messages.error(request, "There is no active discount code to remove.")

    return redirect("view_cart")
