from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, this is the MAKEJID home page.")

def clubs(request):
    return HttpResponse("THIS IS WHERE THE LISTS OF CLUBS GO")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MAKE_JID.base.urls')),
    path('clubs/', clubs),
]
