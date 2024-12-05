from rest_framework.routers import DefaultRouter
from apps.finanzas.api.views import *
routerFinanzas = DefaultRouter()
routerFinanzas.register(prefix='tipos-desecho', viewset=ModelViewSetTiposDesecho)
routerFinanzas.register(prefix='cultivos', viewset=ModelViewSetCultivos)
routerFinanzas.register(prefix='desechos', viewset=ModelViewSetDesechos)
routerFinanzas.register(prefix='cosechas', viewset=ModelViewSetCosechas)
routerFinanzas.register(prefix='ventas', viewset=ModelViewSetVentas)
routerFinanzas.register(prefix='actividades', viewset=ModelViewSetActividades)
routerFinanzas.register(prefix='insumos', viewset=ModelViewSetInsumos)
routerFinanzas.register(prefix='usos-productos', viewset=ModelViewSetUsosProductos)
