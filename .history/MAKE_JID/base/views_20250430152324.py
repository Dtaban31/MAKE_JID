from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# base/views.py

from .forms import SignupForm, LoginForm  # Should be SignupForm not SignUpForm


def home_view(request):
    return render(request, 'base/home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user to the database
            login(request, user)  # Log the user in automatically
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'base/login.html', {'form': form})  # Use the correct path

def create_event(request):
    return render(request, 'base/create_event.html')

