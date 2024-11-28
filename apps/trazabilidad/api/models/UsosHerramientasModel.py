from django.db import models
import HerramientasModel

class UsosHerramientas(models.Model):
    fk_Herramienta = models.ForeignKey(HerramientasModel,on_delete=models.SET_NULL,null=True)
    fk_Actividad = models.IntegerField()
    def __str__(self):
        return str(self.fk_Herramienta) + str(self.fk_Actividad)