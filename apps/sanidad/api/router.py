from rest_framework.routers import DefaultRouter
from apps.sanidad.api.views import TipoPlagaModelViewSet
from apps.sanidad.api.views import PlagaModelViewSet
from apps.sanidad.api.views import AfeccionesModelViewSet
from apps.sanidad.api.views import TiposControlModelViewSet
from apps.sanidad.api.views import ControleslModelViewSet
from apps.sanidad.api.views import ProductosControlModelViewSet
from apps.sanidad.api.views import UsoProductosControlModelViewSet

router_tipoPlaga = DefaultRouter()
router_tipoPlaga.register(prefix='tipoPlaga', basename='tipoPlaga', viewset=TipoPlagaModelViewSet)

router_plaga = DefaultRouter()
router_plaga.register(prefix='plaga', basename='plaga', viewset=PlagaModelViewSet)

router_afecciones = DefaultRouter()
router_afecciones.register(prefix='afecciones', basename='afecciones', viewset=AfeccionesModelViewSet)

router_tiposControl = DefaultRouter()
router_tiposControl.register(prefix='tiposControl', basename='tiposControl', viewset=TiposControlModelViewSet)

router_controles = DefaultRouter()
router_controles.register(prefix='controles', basename='controles', viewset=ControleslModelViewSet)

router_productosControl = DefaultRouter()
router_productosControl.register(prefix='productosControl', basename='productosControl', viewset=ProductosControlModelViewSet)

router_usoProductosControl = DefaultRouter()
router_usoProductosControl.register(prefix='usoproductosControl', basename='usoproductosControl', viewset=UsoProductosControlModelViewSet)


