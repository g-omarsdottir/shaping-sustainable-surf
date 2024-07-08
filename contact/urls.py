from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path(
        "success/<int:contact_id>/",
        views.contact_success,
        name="contact_success"
    ),
]
