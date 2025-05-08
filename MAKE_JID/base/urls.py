from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('rsvp/<int:post_id>/', views.rsvp, name='rsvp'),
]
