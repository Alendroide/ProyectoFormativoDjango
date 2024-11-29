from django.contrib import admin
from apps.sanidad.api.models.tipoPlaga import tipoPlaga
from apps.sanidad.api.models.PlagaModel import Plaga

admin.site.register(tipoPlaga)
admin.site.register(Plaga)
