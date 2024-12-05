from django.contrib import admin
from apps.sanidad.api.models.tipoPlaga import tipoPlaga
from apps.sanidad.api.models.PlagaModel import Plaga
from apps.sanidad.api.models.AfeccionesMoldel import Afecciones
from apps.sanidad.api.models.TiposControlModel import TiposControl


admin.site.register(tipoPlaga)
admin.site.register(Plaga)
admin.site.register(Afecciones)
admin.site.register(TiposControl)