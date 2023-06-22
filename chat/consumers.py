import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import Room, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name, 
            self.channel_name
        )
        
        await self.accept()
    
    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name, 
            self.channel_name
        )
    
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        room_id = text_data_json["room_id"]
        
        room = await self.get_room(room_id)
        user = self.scope["user"]
        message_obj = await self.save_message(user, room, message)
        
        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, 
            {
                "type": "chat_message", 
                "message": message_obj.text,
                "date": str(message_obj.created_at.date()),
                "username": username,
            }
        )
    
    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        date = event["date"]
        
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            "type": "chat_message", 
            "message": str(message),
            "date": str(date),
            "username": str(username),
        }))
    
    @database_sync_to_async
    def get_room(self, room_id):
        return Room.objects.get(id=room_id)
    
    @database_sync_to_async
    def save_message(self, user, room, message):
        return Message.objects.create(user=user, room=room, text=message)