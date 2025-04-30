# base/forms.py

from django import forms
from .models import Event
from django.contrib.auth.forms import UserCreationForm
from .models import Account  # Make sure Account is imported correctly
from django.contrib.auth.forms import AuthenticationForm

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'time', 'location']

class SignupForm(UserCreationForm):  # Changed from SignUpForm to SignupForm
    class Meta:
        model = Account
        fields = ['username', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=150)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
