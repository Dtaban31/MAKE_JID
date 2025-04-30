from django.urls import path
from . import views

urlpatterns = [
    path('create-event/', views.create_event, name='create_event'),
    path('signup/', views.signup_view, name='signup'),
]


