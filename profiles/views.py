from django.shortcuts import render

from .models import UserProfile
from checkout.models import Order


def profile(request):
    """
    Display the user's profile.
    """
    profile = request.user.userprofile
    orders = profile.orders.all().order_by('-date')
    
    context = {
        'profile': profile,
        'orders': orders,
    }
    template = 'profiles/profile.html'

    context = {}

    return render(request, template, context)
