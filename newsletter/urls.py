from django.urls import path
from . import views

urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe"),
    path("unsubscribe/<str:token>/", views.unsubscribe, name="unsubscribe"),
    path(
        "send-newsletter/<int:newsletter_id>/",
        views.send_newsletter,
        name="send_newsletter"
    ),
]
