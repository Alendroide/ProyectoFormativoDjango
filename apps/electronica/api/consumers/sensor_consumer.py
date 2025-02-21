import json
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from apps.electronica.api.models.sensor import Sensor
from apps.electronica.api.models.lote import Lote
from apps.electronica.api.models.era import Eras  


class SensorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Maneja la conexión WebSocket para un sensor específico."""
        self.sensor_id = self.scope['url_route']['kwargs'].get('sensor_id')
        self.room_group_name = f"sensor_{self.sensor_id}" if self.sensor_id else "sensors_global"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()
        print(f"✅ Cliente conectado al grupo {self.room_group_name}")

    async def disconnect(self, close_code):
        """Maneja la desconexión del WebSocket."""
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)
        print(f"❌ Cliente desconectado del grupo {self.room_group_name}")

    async def receive(self, text_data):
        """Procesa los mensajes recibidos del WebSocket."""
        try:
            data = json.loads(text_data)
            action = data.get('action')
            print(f"📥 Mensaje recibido: {data}")

            if action == "register_sensor":
                await self.register_sensor(data)
            elif action == "update_sensor":
                await self.update_sensor(data)
            elif action == "get_sensor":
                await self.get_sensor_by_id(data)
            else:
                await self.send(json.dumps({'error': "❌ Acción no válida"}))
        except json.JSONDecodeError:
            await self.send(json.dumps({'error': "❌ Formato JSON inválido"}))
        except Exception as e:
            print(f"❌ Error en receive: {e}")
            await self.send(json.dumps({'error': f"❌ Error interno: {str(e)}"}))

    async def register_sensor(self, data):
        """Registra un nuevo sensor en la base de datos."""
        try:
            fk_lote_id = data.get('fk_lote')
            fk_eras_id = data.get('fk_eras')
            tipo = data.get('tipo')
            valor = data.get('valor')

            # Validar si el tipo de sensor es válido
            tipos_validos = dict(Sensor.SENSOR_TYPES).keys()
            if tipo not in tipos_validos:
                await self.send(json.dumps({'error': f"❌ Tipo de sensor '{tipo}' no válido. Tipos válidos: {list(tipos_validos)}"}))
                return

            # Validar si el lote y la era existen en la base de datos
            lote = None
            eras = None

            if fk_lote_id:
                lote = await sync_to_async(Lote.objects.filter(id=fk_lote_id).first)()
                if not lote:
                    await self.send(json.dumps({'error': f"❌ Lote {fk_lote_id} no existe"}))
                    return

            if fk_eras_id:
                eras = await sync_to_async(Eras.objects.filter(id=fk_eras_id).first)()
                if not eras:
                    await self.send(json.dumps({'error': f"❌ Era {fk_eras_id} no existe"}))
                    return

            # Crear el sensor en la base de datos
            new_sensor = await sync_to_async(Sensor.objects.create, thread_sensitive=True)(
                fk_lote=lote,
                fk_eras=eras,
                tipo=tipo,
                valor=valor
            )

            sensor_info = {
                "id": new_sensor.id,
                "fk_lote": new_sensor.fk_lote.id if new_sensor.fk_lote else None,
                "fk_eras": new_sensor.fk_eras.id if new_sensor.fk_eras else None,
                "tipo": new_sensor.tipo,
                "valor": float(new_sensor.valor),
                "fecha": new_sensor.fecha.isoformat()
            }

            await self.channel_layer.group_send(
                "sensors_global",
                {"type": "sensor_registered", "sensor_info": sensor_info}
            )

        except Exception as e:
            print(f"❌ Error al registrar sensor: {e}")
            await self.send(json.dumps({'error': f"❌ Error al registrar sensor: {str(e)}"}))

    async def update_sensor(self, data):
        """Actualiza un sensor existente y notifica en tiempo real."""
        sensor_id = data.get('sensor_id')
        valor = data.get('valor')

        if not sensor_id or valor is None:
            await self.send(json.dumps({'error': "❌ Datos insuficientes"}))
            return

        sensor = await self.get_sensor(sensor_id)
        if not sensor:
            await self.send(json.dumps({'error': f"❌ Sensor {sensor_id} no encontrado"}))
            return

        await self.save_sensor(sensor, valor)
        timestamp = datetime.utcnow().isoformat()

        await self.channel_layer.group_send(
            f"sensor_{sensor_id}",
            {
                'type': 'sensor_update',
                'sensor_id': sensor.id,
                'valor': float(sensor.valor),
                'tipo': sensor.tipo,
                'timestamp': timestamp
            }
        )

    async def get_sensor_by_id(self, data):
        """Obtiene un sensor por su ID y lo envía al cliente."""
        sensor_id = data.get('sensor_id')

        if not sensor_id:
            await self.send(json.dumps({'error': "❌ Se requiere un ID de sensor"}))
            return

        try:
            sensor = await sync_to_async(Sensor.objects.get, thread_sensitive=True)(id=sensor_id)
        except Sensor.DoesNotExist:
            await self.send(json.dumps({'error': f"❌ Sensor {sensor_id} no encontrado"}))
            return

        sensor_info = {
            "id": sensor.id,
            "fk_lote_id": sensor.fk_lote.id if sensor.fk_lote else None,
            "fk_eras_id": sensor.fk_eras.id if sensor.fk_eras else None,
            "tipo": sensor.tipo,
            "valor": float(sensor.valor),
            "fecha": sensor.fecha.isoformat()
        }

        await self.send(json.dumps({"sensor_info": sensor_info}))

    async def sensor_update(self, event):
        """Envía actualizaciones a los clientes conectados."""
        await self.send(json.dumps({
            'sensor_id': event['sensor_id'],
            'valor': event['valor'],
            'tipo': event['tipo'],
            'timestamp': event['timestamp']
        }))

    async def sensor_registered(self, event):
        """Envía una notificación cuando se registra un nuevo sensor."""
        await self.send(json.dumps({
            "message": "Nuevo sensor registrado",
            "sensor_info": event["sensor_info"]
        }))

    @sync_to_async
    def get_sensor(self, sensor_id):
        """Obtiene un sensor de la base de datos."""
        try:
            return Sensor.objects.get(id=sensor_id)
        except Sensor.DoesNotExist:
            return None

    @sync_to_async
    def save_sensor(self, sensor, valor):
        """Guarda un nuevo valor en el sensor."""
        sensor.valor = valor
        sensor.save()