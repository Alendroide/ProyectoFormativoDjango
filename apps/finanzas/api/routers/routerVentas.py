from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerVentas import SerializerVentas

routerVentas = DefaultRouter()
routerVentas.register(prefix="/Ventas",viewset=SerializerVentas)