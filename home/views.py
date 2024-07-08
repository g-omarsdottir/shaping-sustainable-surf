from django.views import generic
from django.shortcuts import render


class Index(generic.TemplateView):
    """
    Display the homepage
    **Context**
        ``home``
    ***Template:***
    :template:`index.html`
    """

    template_name = "home/index.html"
