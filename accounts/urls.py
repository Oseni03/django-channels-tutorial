from django.urls import path 
from django.contrib.auth import views as auth_views
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", FormView.as_view(
        template_name="registration/register.html", 
        form_class=UserCreationForm, 
        success_url="chat2/home/"
        ), name="register"),
]