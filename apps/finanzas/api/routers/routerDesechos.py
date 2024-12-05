from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerDesechos import SerializerDesechos

routerDesechos = DefaultRouter()
routerDesechos.register(prefix="desechos",viewset=SerializerDesechos)