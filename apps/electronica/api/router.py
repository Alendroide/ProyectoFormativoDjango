from rest_framework.routers import DefaultRouter
from apps.electronica.api.views import *

router_lote = DefaultRouter()
router_lote.register(prefix= 'lote', viewset= LoteView, basename='lote')

router_era = DefaultRouter()
router_era.register(prefix='eras', viewset=Erasview, basename='eras')

router_sensor = DefaultRouter()
router_sensor.register(prefix='sensor',viewset=sensoresview, basename='sensor')

router_HumedadTerreno = DefaultRouter()
router_HumedadTerreno.register(prefix='HumedadTerreno', viewset=HumedadTerrenoview, basename='HumedadTerreno')

router_ph = DefaultRouter()
router_ph.register(prefix='ph', viewset=Phview, basename='ph')
