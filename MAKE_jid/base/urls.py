from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),  # Home page route
    path('create-event/', views.create_event, name='create_event'),  # Create event route
    path('signup/', views.signup_view, name='signup'),  # Signup route
    path('login/', views.login_view, name='login'),  # Login route
]
