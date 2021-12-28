from .views import Login, register, index
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", index, name="index"),
    path("signup/", register, name="register"),
    path("login/", Login, name="login"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="login.html"),
        {"next_page": "index"},
        name="logout",
    ),
]
