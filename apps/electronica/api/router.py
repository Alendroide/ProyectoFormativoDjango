from rest_framework.routers import DefaultRouter
from apps.electronica.api.views import *

routerElectronica = DefaultRouter()
routerElectronica.register(prefix= 'lote', viewset= LoteView, basename='lote')
routerElectronica.register(prefix='eras', viewset=Erasview, basename='eras')
routerElectronica.register(prefix='sensor',viewset=sensoresview, basename='sensor')
routerElectronica.register(prefix='HumedadTerreno', viewset=HumedadTerrenoview, basename='HumedadTerreno')
routerElectronica.register(prefix='ph', viewset=Phview, basename='ph')