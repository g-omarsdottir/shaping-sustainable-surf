from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
    path(
        "newsletter_success/",
        views.newsletter_success,
        name="newsletter_success"
    ),
]
