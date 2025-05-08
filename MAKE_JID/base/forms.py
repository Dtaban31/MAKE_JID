from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginForm(AuthenticationForm):
    pass  # You can customize if needed


class SignupForm(UserCreationForm):
    pass  # You can customize if needed
