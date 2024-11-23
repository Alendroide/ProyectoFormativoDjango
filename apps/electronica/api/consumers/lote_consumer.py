import json
from channels.generic.websocket import AsyncWebsocketConsumer
from apps.electronica.api.models.sensor import Sensor

class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'sensor_updates'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()