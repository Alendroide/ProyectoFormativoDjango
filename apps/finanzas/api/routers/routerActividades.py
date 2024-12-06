from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerActividades import SerializerActividades

routerActividades = DefaultRouter()
routerActividades.register(prefix="Actividades",viewset=SerializerActividades)