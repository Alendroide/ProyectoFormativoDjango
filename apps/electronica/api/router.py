from rest_framework.routers import DefaultRouter
from apps.electronica.api.views import *

router_Electronica = DefaultRouter()
router_Electronica.register(prefix= 'lote', viewset= LoteView, basename='lote')
router_Electronica.register(prefix='eras', viewset=Erasview, basename='eras')
router_Electronica.register(prefix='sensor',viewset=sensoresview, basename='sensor')
router_Electronica.register(prefix='HumedadTerreno', viewset=HumedadTerrenoview, basename='HumedadTerreno')
router_Electronica.register(prefix='ph', viewset=Phview, basename='ph')
