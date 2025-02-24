from channels.generic.websocket import AsyncWebSocketConsumer
import json 

class ChatConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat%s' % self.room_name 
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self):
        await self.channel_layer.group_discard(
        self.room_group_name,
        self.channel_name
        )


    async def receive(self,text_data):
        data=json.loads(text_data)
        message=data['message']
        username=data['username']
        room=data['room']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'username':username,
                'room':room,
            }
        )


    async def chat_message(self,event):
        message=event['message']
        username=event['username']
        room=event['room']

        await self.send(text_data=json.dump({
                'message':message,
                'username':username,
                'room':room,
        }))


