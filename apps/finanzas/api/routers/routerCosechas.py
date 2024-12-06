from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerCosechas import SerializerCosechas

routerCosechas = DefaultRouter()
routerCosechas.register(prefix="cosechas",viewset=SerializerCosechas,basename="cosechas")