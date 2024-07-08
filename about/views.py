from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import AboutUs, FAQ, CustomSurfboard, Resource


class AboutUsView(TemplateView):
    """
    View to display the About Us content.
    Related to :model:`about.AboutUs`
     **Context**
        ``about_content`` - About Us content.
    ***Template:***
    :template:`about/about.html`
    """

    model = AboutUs
    template_name = "about/about.html"
    context_object_name = "about_content"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_content'] = AboutUs.objects.first()
        return context


class FAQListView(ListView):
    """
    View to display the FAQ content.
    Related to :model:`about.FAQ`
    **Context**
    ``faq`` - FAQ content.
    ***Template:***
    :template:`about/faq.html`
    """

    model = FAQ
    template_name = "about/faq.html"
    context_object_name = "faq"


class CustomSurfboardListView(ListView):
    """
    View to display the Custom Surfboard content.
    Related to :model:`about.CustomSurfboard`
    **Context**
    ``surfboards`` - Custom Surfboard content.
    ***Template:***
    :template:`about/custom_surfboard_list.html`
    """

    model = CustomSurfboard
    template_name = "about/custom_surfboard_list.html"
    context_object_name = "custom_surfboards"


class CustomSurfboardDetailView(DetailView):
    """
    View to display the Custom Surfboard detail.
    Related to :model:`about.CustomSurfboard`
    **Context**
    ``surfboard`` - Custom Surfboard detail.
    ***Template:***
    :template:`about/custom_surfboard_detail.html`
    """

    model = CustomSurfboard
    template_name = "about/custom_surfboard_detail.html"
    context_object_name = "surfboard"


class ResourceListView(ListView):
    """
    View to display the Resources content.
    Related to :model:`about.Resource`
    **Context**
    ``resources`` - Resources content.
    ***Template:***
    :template:`about/resources.html`
    """

    model = Resource
    template_name = "about/resources.html"
    context_object_name = "resources"
