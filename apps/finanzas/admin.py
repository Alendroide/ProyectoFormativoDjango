from django.contrib import admin
from apps.finanzas.models import TiposDesecho, Cultivos, Desechos, Cosechas, Ventas, Actividades, Insumos, UsosProductos
# Register your models here.

admin.site.register(TiposDesecho)
admin.site.register(Cultivos)
admin.site.register(Desechos)
admin.site.register(Cosechas)
admin.site.register(Ventas)
admin.site.register(Actividades)
admin.site.register(Insumos)
admin.site.register(UsosProductos)
