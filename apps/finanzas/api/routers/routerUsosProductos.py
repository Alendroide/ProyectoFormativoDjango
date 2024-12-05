from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerUsosProductos import SerializerUsosProductos

routerUsosProductos = DefaultRouter()
routerUsosProductos.register(prefix="/usos-productos",viewset=SerializerUsosProductos)