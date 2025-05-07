from django.shortcuts import render


# Create your views here.
rooms = [
    {'id': 1, 'name':'Login'},
    {'id': 2, 'name':'Post Creation'},
]



def home(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html', context)

def clubs(request, pk):

    room = None
    for i in rooms:
        if i['id']== int(pk):
            room = i
    context = {'room': room}
    return render(request,'base/clubs.html', context)
