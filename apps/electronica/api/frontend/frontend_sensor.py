import asyncio
import websockets
import json
import random
import datetime

URI = "ws://127.0.0.1:8000/ws/sensor/"

async def send_sensor_data(websocket):
    """Envía datos simulados de sensores periódicamente"""
    while True:
        try:
            sensor_data = {
                "sensor_id": random.randint(1, 5),  # Simula sensores con ID del 1 al 5
                "valor": round(random.uniform(20.0, 40.0), 2)  # Simula valores entre 20 y 40
            }

            await websocket.send(json.dumps(sensor_data))
            print(f"📤 Enviado: {sensor_data}")

            # Esperar un tiempo antes de la siguiente actualización
            await asyncio.sleep(5)

        except websockets.ConnectionClosed:
            print("❌ Conexión cerrada, intentando reconectar...")
            break  # Sale del loop y se reconectará en `connect()`

async def receive_sensor_data(websocket):
    """Escucha datos del servidor WebSocket"""
    while True:
        try:
            data = await websocket.recv()
            data = json.loads(data)

            if "error" in data:
                print('❌ Error del servidor:', data["error"])
            else:
                print(f'📡 Recibido: Sensor {data["sensor_id"]} -> {data["valor"]} ({data["timestamp"]})')

        except websockets.ConnectionClosed:
            print("❌ Conexión cerrada por el servidor.")
            break

async def connect():
    """Maneja la conexión al WebSocket con reintentos"""
    while True:
        try:
            async with websockets.connect(URI) as websocket:
                print('✅ Conexión establecida al WebSocket.')

                # Lanzar en paralelo el envío y recepción de datos
                await asyncio.gather(
                    send_sensor_data(websocket),
                    receive_sensor_data(websocket)
                )

        except Exception as e:
            print(f'❌ Error de conexión: {e}, reintentando en 5 segundos...')
            await asyncio.sleep(5)  # Espera antes de reintentar la conexión

# Iniciar la conexión WebSocket
asyncio.run(connect())