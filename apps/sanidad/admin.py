from django.contrib import admin
from apps.sanidad.models import TipoPlaga, Plaga, Afecciones, TiposControl, Controles, ProductosControl, UsoProductosControl

admin.site.register(TipoPlaga)
admin.site.register(Plaga)
admin.site.register(Afecciones)
admin.site.register(TiposControl)
admin.site.register(Controles)
admin.site.register(ProductosControl)
admin.site.register(UsoProductosControl)


