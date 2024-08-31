from django.urls import path
from . import views

urlpatterns = [
    path("subscribe/", views.subscribe, name="subscribe"),
    path("unsubscribe/<str:token>/", views.unsubscribe, name="unsubscribe"),
]
