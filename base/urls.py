from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('clubs/<str:pk>/', views.clubs, name="clubs"),


]



