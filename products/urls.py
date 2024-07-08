from django.urls import path
from . import views

urlpatterns = [
    path("tutorials/", views.tutorials_list, name="tutorials_list"),
    path(
        "product/<int:product_id>/",
        views.tutorial_detail,
        name="tutorial_detail"
    ),
]
