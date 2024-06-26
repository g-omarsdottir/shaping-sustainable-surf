from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Subcategory

# Views


def tutorials_list(request):
    """
    A view to display overview of tutorials.
    Objects to display from model Product 
        are filtered by category and status.
    """

    tutorials = Product.objects.filter(status="Publish", category__name="Tutorial")
    template_name = "products/tutorials.html"
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"

            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "subcategory" in request.GET:
            subcategories = request.GET["subcategory"].split(",")
            products = products.filter(subcategory__name__in=subcategories)
            subcategories = Subcategory.objects.filter(name__in=subcategories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    # return the current sorting methodology to the template
    current_sorting = f"{sort}_{direction}" if sort and direction else "None_None"

    # So products will be available in the template
    context = {
        "tutorials": tutorials,
        "search_term": query,
        "current_categories": categories,
        "current_subcategories": subcategories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/tutorials.html", context)

def product_detail(request, product_id):
    """
    A view to display individual product details.
    Template to display: products/product_detail.html
    Related to templates products/tutorials.html 
        and products/surfboards.
    """

    # Return from datbase - here no filtering, returning all products
    product = get_object_or_404(Product, pk=product_id)

    # Add products to the context, so the products will be available in the template
    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)
