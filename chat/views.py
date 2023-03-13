from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Room, Message

# Create your views here.
def index(request):
    if request.method == "POST":
        room_name = request.POST.get("room_name")
        room = Room.objects.get_or_create(name=room_name)[0]
        return redirect(room.get_absolute_url())
    return render(request, "chat/index.html")

@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.select_related("user").filter(room=room)
    return render(request, "chat/room.html", {"room": room, "messages": messages})