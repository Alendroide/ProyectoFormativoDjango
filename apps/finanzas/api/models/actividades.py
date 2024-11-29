from django.db import models
from apps.finanzas.api.models.cultivos import Cultivos
from apps.users.models import Usuario

class Actividades(models.Model):
    fk_Cultivo = models.ForeignKey(Cultivos, on_delete = models.SET_NULL, null= True)
    fk_Usuario=models.ForeignKey(Usuario, on_delete= models.SET_NULL,null=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    fecha =models.DateField(auto_now=False)
    def __str__(self):
        return self.titulo