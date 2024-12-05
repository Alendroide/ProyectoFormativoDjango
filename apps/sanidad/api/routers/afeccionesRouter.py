from rest_framework.routers import DefaultRouter
from apps.sanidad.api.views.afeccionesViews import AfeccionesModelSerializer

router_afecciones = DefaultRouter()
router_afecciones.register(prefix='afecciones', basename='afecciones', viewset=AfeccionesModelSerializer)