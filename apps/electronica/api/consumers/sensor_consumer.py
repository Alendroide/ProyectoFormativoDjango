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

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        sensor_id = text_data_json['sensor_id']
        sensor_value = text_data_json['valor']

        try:
            sensor = Sensor.objects.get(id=sensor_id)
            sensor.valor = sensor_value
            sensor.save()

            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'sensor_update',
                    'sensor_id': sensor.id,
                    'valor': sensor.valor,
                }
            )
        except Sensor.DoesNotExist:
            pass
    
    async def sensor_update(self, event):

        sensor_id = event['sensor_id']
        valor = event['valor']

        await self.send(text_data=json.dumps({
            'sensor_id': sensor_id,
            'valor': valor,
        }))