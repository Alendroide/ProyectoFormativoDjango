from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerCultivos import SerializerCultivos

routerCultivos = DefaultRouter()
routerCultivos.register(prefix="cultivos",viewset=SerializerCultivos)