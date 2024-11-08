from django.contrib import admin
from apps.sanidad.models import TipoPlaga
from apps.sanidad.models import Plaga
from apps.sanidad.models import Afecciones
from apps.sanidad.models import TiposControl
from apps.sanidad.models import Controles
from apps.sanidad.models import ProductosControl
from apps.sanidad.models import UsoProductosControl

admin.site.register(TipoPlaga)
admin.site.register(Plaga)
admin.site.register(Afecciones)
admin.site.register(TiposControl)
admin.site.register(Controles)
admin.site.register(ProductosControl)
admin.site.register(UsoProductosControl)


