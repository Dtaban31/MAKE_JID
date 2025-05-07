from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-event/', views.create_event, name='create_event'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
