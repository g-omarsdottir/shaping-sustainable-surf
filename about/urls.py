from django.urls import path
from . import views

urlpatterns = [
    path("", views.AboutUsView.as_view(), name="about_content"),
    path("faq/", views.FAQListView.as_view(), name="faq"),
    path(
        "custom-surfboards/",
        views.CustomSurfboardListView.as_view(),
        name="custom_surfboards"
    ),
    path(
        "custom-surfboards/<slug:slug>/",
        views.CustomSurfboardDetailView.as_view(),
        name="custom_surfboard_detail"
    ),
    path("resources/", views.ResourceListView.as_view(), name="resources"),
]
