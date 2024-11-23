from django.db import models
import math

class Lote(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.TextField()
    tamX = models.PositiveSmallIntegerField()
    tamY = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)
    posX = models.DecimalField(max_digits=6, decimal_places=2)
    posY = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.nombre

    def calcular_evapotranspiracion(self):
        try:
            temperatura = self.sensores.filter(tipo='TEM').latest('fecha').valor  
            humedad_relativa = self.sensores.filter(tipo='HUM_A').latest('fecha').valor  
            radiacion_solar = self.sensores.filter(tipo='LUM').latest('fecha').valor  
            velocidad_viento = self.sensores.filter(tipo='VIE').latest('fecha').valor  

            velocidad_viento = velocidad_viento * 1000 / 3600  
            radiacion_solar = radiacion_solar * 0.0864  

            elevacion = 1000
            es = 0.6108 * math.exp((17.27 * temperatura) / (temperatura + 237.3))
            ea = es * (humedad_relativa / 100)
            delta = (4098 * es) / ((temperatura + 237.3) ** 2)
            gamma = 0.665 * 10 ** -3 * (101.3 * ((293 - (0.0065 * elevacion)) / 293) ** 5.26)

            ET0 = (0.408 * delta * radiacion_solar + gamma * (900 / (temperatura + 273)) * velocidad_viento * (es - ea)) \
                / (delta + gamma * (1 + 0.34 * velocidad_viento))

            return round(ET0, 2)
        except self.sensores.model.DoesNotExist:
            return "No hay datos suficientes para calcular la evapotranspiración."
