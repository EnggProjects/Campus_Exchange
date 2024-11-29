# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm, LoginForm
from django.utils import timezone
from auctions.models import Auction
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm


def home(request):
    print("Home view is being called!")
    current_time = timezone.now()
    active_auctions = Auction.objects.filter(end_time__gt=current_time)
    return render(request, 'home.html', {'active_auctions': active_auctions})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log in the user after registration
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the errors below.')
            print(form.errors)  # Print form errors for debugging
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been logged in.')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('home')


@login_required
def profile(request):
    context = {
        'user': request.user,
        'products_count': request.user.products_count,
    }
    return render(request, 'users/profile.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }
    return render(request, 'users/update_profile.html', context)