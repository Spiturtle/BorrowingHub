from django.shortcuts import render, redirect
from django.contrib import messages
from registration_app.models import TblUser

def dashboard_view(request):
    # Check session-based authentication
    user_id = request.session.get('user_id')
    
    if not user_id:
        messages.error(request, 'Please log in to access the dashboard.')
        return redirect('login_app:login')
    
    try:
        user = TblUser.objects.get(id=user_id)
    except TblUser.DoesNotExist:
        request.session.flush()
        messages.error(request, 'Invalid session. Please log in again.')
        return redirect('login_app:login')
    
    context = {
        'user': user,
        'total_items': 0,
        'available_items': 0,
        'borrowed_items': 0,
        'overdue_items': 0,
    }
    return render(request, 'dashboard_app/dashboard.html', context)

def profile_view(request):
    # Check session-based authentication
    user_id = request.session.get('user_id')
    
    if not user_id:
        messages.error(request, 'Please log in to access your profile.')
        return redirect('login_app:login')
    
    try:
        user = TblUser.objects.get(id=user_id)
    except TblUser.DoesNotExist:
        request.session.flush()
        messages.error(request, 'Invalid session. Please log in again.')
        return redirect('login_app:login')
    
    context = {
        'user': user,
    }
    return render(request, 'profile_app/profile.html', context)