from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerPasantes import SerializerPasantes

routerPasantes= DefaultRouter()
routerPasantes.register(prefix='Pasantes',viewset=SerializerPasantes)
