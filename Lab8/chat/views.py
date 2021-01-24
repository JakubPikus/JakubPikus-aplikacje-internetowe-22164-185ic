from django.shortcuts import render


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def worker1(request):
     return render(request, 'webWorker/worker1.html', {})

def worker2(request):
     return render(request, 'webWorker/worker2.html', {})
