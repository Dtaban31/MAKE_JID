from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, RSVP
from .forms import LoginForm, SignupForm


# Home Page View
def home(request):
    """
    Displays all posts (events) on the homepage.
    Includes login/signup forms if the user is not authenticated.
    """
    posts = Post.objects.all()  # Fetch all events (posts)
    login_form = LoginForm()
    signup_form = SignupForm()

    # Build a dictionary to track which posts the user RSVP'd to
    user_rsvps = set()
    if request.user.is_authenticated:
        user_rsvps = set(
            RSVP.objects.filter(user=request.user).values_list('post_id', flat=True)
        )

    return render(request, 'base/home.html', {
        'posts': posts,
        'login_form': login_form,
        'signup_form': signup_form,
        'user_rsvps': user_rsvps,  # Pass RSVP data to template
    })



# RSVP View
@login_required
def rsvp(request, post_id):
    """
    Allows a logged-in user to RSVP to a specific post (event).
    If already RSVP'd, no duplicate RSVP is created.
    """
    post = get_object_or_404(Post, id=post_id)  # Fetch the specific event
    RSVP.objects.get_or_create(user=request.user, post=post)  # Track RSVP
    return redirect('home')  # Redirect back to the homepage


# Login/Signup Logic in One View
def login_signup_view(request):
    """
    Processes login and signup actions on the homepage.
    Handles two forms: LoginForm and SignupForm.
    If valid, redirects the user to the homepage.
    """
    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == 'POST':
        # Handle login form submission
        if 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect('home')

        # Handle signup form submission
        elif 'signup' in request.POST:
            signup_form = SignupForm(data=request.POST)
            if signup_form.is_valid():
                # Create a new user and log them in
                user = signup_form.save()
                login(request, user)
                return redirect('home')

    return render(request, 'base/home.html', {  # UPDATED PATH
        'login_form': login_form,
        'signup_form': signup_form,
    })
