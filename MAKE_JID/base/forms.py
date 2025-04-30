# base/forms.py

from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from .models import Account  # Make sure Account is imported correctly

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']

class SignUpForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']
