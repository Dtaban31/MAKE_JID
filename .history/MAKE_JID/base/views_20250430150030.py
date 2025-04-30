from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm  # assuming you have forms defined

def home_view(request):
    return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Process the form
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process the form
            return redirect('home')  # Redirect to the home page after login
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
