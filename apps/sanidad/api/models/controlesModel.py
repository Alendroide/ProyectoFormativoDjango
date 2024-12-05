from django.db import models;
from apps.sanidad.api.models.AfeccionesMoldel import Afecciones;
from apps.sanidad.api.models.TiposControlModel import TiposControl;



class Controles(models.Model):
    fk_Afeccion = models.ForeignKey(Afecciones, on_delete=models.SET_NULL, null=True)
    fk_TipoControl = models.ForeignKey(
        TiposControl, on_delete=models.SET_NULL, null=True
    )
    descripcion = models.TextField()
    fechaControl = models.DateField()

    def __str__(self):
        return self.descripcion
