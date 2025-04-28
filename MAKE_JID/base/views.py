from django.shortcuts import render

# Create your views here.

# base/views.py

from django.shortcuts import render, redirect
from .forms import EventForm
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
