from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    if request.session.get('user_id'):
        return redirect('dashboard_app:dashboard')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            # Success message and redirect to login (NO auto-login)
            messages.success(request, f'Account created for {username}! Please log in.')
            return redirect('login_app:login')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration_app/register.html', {'form': form})