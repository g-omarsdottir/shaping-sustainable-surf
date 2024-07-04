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

    print(context)
    print(f"Video unlocked: {profile.video_unlocked}")

    return render(request, template, context)
