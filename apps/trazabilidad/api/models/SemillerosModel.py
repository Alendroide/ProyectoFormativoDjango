from django.db import models
import EspeciesModel

class Semilleros(models.Model):
    fk_Especie = models.ForeignKey(EspeciesModel,on_delete=models.SET_NULL,null=True)
    unidades = models.IntegerField()
    fechaSiembra = models.DateField()
    fechaEstimada = models.DateField()
    def __str__(self):
        return ('Semillero de especie:'+str(self.fk_Especie))
