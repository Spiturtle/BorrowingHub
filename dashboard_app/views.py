from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def dashboard_view(request):
    context = {
        'user': request.user,
        'total_items': 0,        # Placeholder for total items
        'available_items': 0,    # Placeholder for available items
        'borrowed_items': 0,     # Placeholder for borrowed items
        'overdue_items': 0,      # Placeholder for overdue items
    }
    return render(request, 'dashboard_app/dashboard.html', context)

@login_required
def profile_view(request):
    context = {
        'user': request.user,
    }
    return render(request, 'profile_app/profile.html', context)
