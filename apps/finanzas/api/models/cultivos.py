from django.db import models

class Cultivos(models.Model):
    nombre = models.CharField(max_length=30)
    unidades = models.IntegerField()
    fechaSiembra = models.DateField(auto_now=False)
    def __str__(self):
        return self.nombre