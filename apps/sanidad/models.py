from django.db import models

class TipoPlaga(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Plaga(models.Model):
    fk_Tipo = models.ForeignKey(TipoPlaga, on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    img = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre
    
class Afecciones(models.Model):
    estado_choises = [
        ('ST','ST'),
        ('EC','EC'),
        ('EL','EL')
    ]
    
    fk_Plantacion = models.IntegerField()
    fk_Plaga = models.ForeignKey(Plaga, on_delete=models.SET_NULL, null=True)
    fechaEncuentro = models.DateField()
    estado = models.CharField(max_length=30, choices=estado_choises, default='ST')
    
    def __str__(self):
        return self.fechaEncuentro
    
class TiposControl(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
class Controles(models.Model):    
    fk_Afeccion = models.ForeignKey(Afecciones, on_delete=models.SET_NULL, null=True)
    fk_TipoControl = models.ForeignKey(TiposControl, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField()
    fechaControl = models.DateField()
    
    def __str__(self):
        return self.descripcion

class ProductosControl(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    compuestoActivo = models.CharField(max_length=20)
    fichaTecnica = models.TextField()
    contenido = models.IntegerField()
    tipoContenido = models.CharField(max_length=10)
    unidades = models.SmallIntegerField()
    
    def __str__(self):
        return self.nombre
    
class UsoProductosControl(models.Model):
    fk_ProductoControl = models.ForeignKey(ProductosControl, on_delete=models.SET_NULL, null=True)
    fk_Control = models.ForeignKey(Controles, on_delete=models.SET_NULL, null=True)
    cantidadProducto = models.IntegerField()

    def __str__(self):
        return self.cantidadProducto    