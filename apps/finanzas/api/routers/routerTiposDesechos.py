from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerTiposDesecho import SerializerTiposDesecho

routertiposserializerTiposDesecho = DefaultRouter()
routertiposserializerTiposDesecho.register(prefix="/tipos-desechos",viewset=SerializerTiposDesecho)