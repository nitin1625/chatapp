from channels.generic.websocket import AsyncWebSocketConsumer
import json 

class ChatConsumer(AsyncWebSocketConsumer):
    async def connect(self):
        self.room_name=self.scope['url_route']['kwargs']['room_name']
        self.room_group_name='chat%s' % self.room_name 
        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )
        await self.accect()

    

