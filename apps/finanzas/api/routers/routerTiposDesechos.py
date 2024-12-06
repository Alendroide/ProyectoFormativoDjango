from rest_framework.routers import DefaultRouter
from apps.finanzas.api.serializers.serializerTiposDesecho import SerializerTiposDesecho

routerTiposDesecho = DefaultRouter()
routerTiposDesecho.register(prefix="tipos-desechos",viewset=SerializerTiposDesecho,basename="tipos-desechos")