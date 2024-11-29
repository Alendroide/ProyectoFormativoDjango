from django.db import models
from apps.users.models import Usuario
# Modelo de la tabla Tipos de desechos. 

    
class Cultivos(models.Model):
    nombre = models.CharField(max_length=30)
    unidades = models.IntegerField()
    fechaSiembra = models.DateField(auto_now=False)
    def __str__(self):
        return self.nombre
# Modelo de la tabla desechos.
class Desechos(models.Model):
    fk_Cultivo = models.ForeignKey(Cultivos, on_delete = models.SET_NULL, null= True)
    fk_TipoDesecho = models.ForeignKey(TiposDesecho, on_delete=models.SET_NULL, null= True)
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    def __str__(self):
        return self.nombre
    
# Modelo de la tabla cosechas.
class Cosechas(models.Model):
    fk_Cultivo = models.ForeignKey(Cultivos, on_delete = models.SET_NULL, null= True)
    unidades = models.IntegerField()
    fecha = models.DateField(auto_now=False)
    def __str__(self):
        return self.fecha


# Modelo de la tabla ventas.
class Ventas(models.Model):
    fk_Cosecha = models.ForeignKey(Cosechas, on_delete=models.SET_NULL, null=True)
    precioUnitario = models.IntegerField()
    fecha =models.DateField(auto_now=False)
    def __str__(self):
        return self.fecha

#modelo de la tabla actividades.
class Actividades(models.Model):
    fk_Cultivo = models.ForeignKey(Cultivos, on_delete = models.SET_NULL, null= True)
    fk_Usuario=models.ForeignKey(Usuario, on_delete= models.SET_NULL,null=True)
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=200)
    fecha =models.DateField(auto_now=False)
    def __str__(self):
        return self.titulo
    
#modelo de la tabla insumos. 
class Insumos(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(max_length=150)
    precio = models.IntegerField()
    unidades = models.IntegerField()
    def __str__(self):
        return self.nombre
    
#modelo de la tabla Usos Productos.
class UsosProductos(models.Model):
    fk_Insumo = models.ForeignKey(Insumos, on_delete=models.SET_NULL, null=True)
    fk_Actividad = models.ForeignKey(Actividades, on_delete=models.SET_NULL, null=True)
    cantidadProducto = models.IntegerField()
    def __str__(self):
        return f"insumo: {self.fk_Insumo}-Cantidad: {self.cantidadProducto}-Actividad: {self.fk_Actividad}"
