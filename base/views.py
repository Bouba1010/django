from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
from .forms import RoomForm

"""
rooms=[
    {
        'id':1,
        'name':'apprendre python',
        
    },
    {
        'id':2,
        'name':'apprendre JAVA',
        
    },
    {
        'id':3,
        'name':'apprendre PHP',
        
    }
]
"""

def home(request):
    #return HttpResponse('Bienvenue')
    rooms= Room.objects.all()
    return render(request,'base/home.html' , {'salons':rooms})
def room(request,pk):
    """room = None
    for salon in rooms:
        if salon ['id'] == int(pk):
            room=salon"""
    room= Room.objects.get(id=pk)
    
    #return HttpResponse('Bienvenue dans le salon')
    return render(request,'base/room.html',{'salon':room})
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        #print(request.post)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request,'base/room_form.html',context)
# Create your views here.
