from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import CustomUserCreationForm   # ✅ your custom form
from django.contrib.auth.forms import AuthenticationForm


# Register
def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect("blog")  # redirect to homepage
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("blog")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    return redirect("blog")

