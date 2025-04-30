from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EventForm, SignUpForm
from django.contrib.auth.decorators import login_required

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.account = request.user  # link event to the logged-in account
            event.save()
            return redirect('home')  # or wherever you want
    else:
        form = EventForm()

    return render(request, 'base/create_event.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # after signup, send them to login page
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})

def home(request):
    return render(request, 'base/home.html')
