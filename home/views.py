from django.views import generic
from django.shortcuts import render


# Create your views here.
class Index(generic.TemplateView):
    """
    Display the homepage
    **Context**
        ``home``
    ***Template:***
    :template:`index.html`
    """

    template_name = "home/index.html"
