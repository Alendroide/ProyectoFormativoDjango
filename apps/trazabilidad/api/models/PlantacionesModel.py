from django.db import models

class Plantaciones(models.Model):
    fk_Cultivo = models.IntegerField()
    fk_Era = models.IntegerField
    creado = models.DateTimeField(auto_now=True)
    def __str__(self):
        return (str(self.fk_Cultivo) + str(self.fk_Era) + str(self.creado))