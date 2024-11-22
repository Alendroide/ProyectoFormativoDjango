from rest_framework.routers import DefaultRouter
from apps.sanidad.api.views import TipoPlagaModelViewSet
from apps.sanidad.api.views import PlagaModelViewSet
from apps.sanidad.api.views import AfeccionesModelViewSet
from apps.sanidad.api.views import TiposControlModelViewSet
from apps.sanidad.api.views import ControleslModelViewSet
from apps.sanidad.api.views import ProductosControlModelViewSet
from apps.sanidad.api.views import UsoProductosControlModelViewSet

routerSanidad = DefaultRouter()

routerSanidad.register(prefix='tipoPlaga', basename='tipoPlaga', viewset=TipoPlagaModelViewSet)
routerSanidad.register(prefix='plaga', basename='plaga', viewset=PlagaModelViewSet)
routerSanidad.register(prefix='afecciones', basename='afecciones', viewset=AfeccionesModelViewSet)
routerSanidad.register(prefix='tiposControl', basename='tiposControl', viewset=TiposControlModelViewSet)
routerSanidad.register(prefix='controles', basename='controles', viewset=ControleslModelViewSet)
routerSanidad.register(prefix='productosControl', basename='productosControl', viewset=ProductosControlModelViewSet)
routerSanidad.register(prefix='usoproductosControl', basename='usoproductosControl', viewset=UsoProductosControlModelViewSet)
