# chat/urls.py
from django.urls import path
from . import views


app_name = "timer"

urlpatterns = [
    path("", views.index, name="index"),
]