from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Register view
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)  # log the user in after registration
            return redirect("/")  # redirect to homepage
    return render(request, "accounts/register.html")

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/dashboard/")  # redirect to dashboard after login
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "accounts/login.html")

# Logout view
def logout_view(request):
    logout(request)
    return redirect("/login/")

# Landing page
def landing_view(request):
    return render(request, "accounts/landing.html")

# Dashboard page
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")
