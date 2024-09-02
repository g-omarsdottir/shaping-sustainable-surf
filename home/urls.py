from django.urls import path
from . import views
from .views import Index, privacy_policy

urlpatterns = [
    path("", views.Index.as_view(), name="home"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),
]
