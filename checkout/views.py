from django.shortcuts import render

# Create your views here.
def checkout(request):
    # No need to pass any context variables for now
    return render(request, 'checkout/checkout.html')

