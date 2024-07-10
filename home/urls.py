from django.urls import path
from . import views
from .views import Index

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy")
]
