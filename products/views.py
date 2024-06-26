from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Subcategory

# Views


def all_products(request):
    """
    Display overview of products.
    """

    products = Product.objects.filter(status="Publish")
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
    if sort is not None and direction is not None:
        current_sorting = f"{sort}_{direction}"
    elif sort is not None:
        current_sorting = sort
    elif direction is not None:
        current_sorting = direction
    else:
        current_sorting = "None_None"

    # So products will be available in the template
    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_subcategories": subcategories,
        "current_sorting": current_sorting,
    }
    return render(request, "products/tutorials.html", context)
