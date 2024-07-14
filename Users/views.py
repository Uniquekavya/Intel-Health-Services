# Users/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from Users.models import UserProfile
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .forms import UserForm, UserProfileForm



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('hospital_list')  # Redirect to your main page after login
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def dashboard(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('dashboard')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=profile)
    
    return render(request, 'users/dashboard.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

