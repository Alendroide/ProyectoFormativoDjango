from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerHorasMensuales import SerializerHorasMensuales

routerHorasMensuales = DefaultRouter()
routerHorasMensuales.register(prefix="/horas-mensuales",viewset=SerializerHorasMensuales)