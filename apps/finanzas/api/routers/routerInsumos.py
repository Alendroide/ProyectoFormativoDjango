from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerInsumos import SerializerInsumos

routerInsumos = DefaultRouter()
routerInsumos.register(prefix="insumos",viewset=SerializerInsumos,basename="insumos")