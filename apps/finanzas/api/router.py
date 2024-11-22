from rest_framework.routers import DefaultRouter
from apps.finanzas.api.views import *
router = DefaultRouter()
router.register(prefix='tipos-desecho', viewset=ModelViewSetTiposDesecho)
router.register(prefix='cultivos', viewset=ModelViewSetCultivos)
router.register(prefix='desechos', viewset=ModelViewSetDesechos)
router.register(prefix='cosechas', viewset=ModelViewSetCosechas)
router.register(prefix='ventas', viewset=ModelViewSetVentas)
router.register(prefix='actividades', viewset=ModelViewSetActividades)
router.register(prefix='insumos', viewset=ModelViewSetInsumos)
router.register(prefix='usos-productos', viewset=ModelViewSetUsosProductos)
