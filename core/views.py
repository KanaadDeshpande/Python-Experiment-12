from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, LoginForm
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

# Create your views here.


def index(request):
    try:
        user = request.user
    except:
        user = "AnonymousUser"
    return render(request, "index.html", {"title": "index", "user": user})


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "register.html", {"form": form, "title": "Sign up"})


def Login(request):
    if request.method == "POST":

        email = request.POST.get("email")
        try:
            validate_email(email)
        except ValidationError as e:
            print("Bad email, details:", e)
        else:
            print("Good email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            form = login(request, user)
            return redirect("index")
        else:
            return redirect("login")
    else:
        form = LoginForm()
        return render(request, "login.html", {"form": form, "title": "Log in"})
