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


class Eras(models.Model):
    fk_lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True) 
    tipo = models.CharField(max_length=20)
    tamX = models.DecimalField(max_digits=6, decimal_places=2)
    tamY = models.DecimalField(max_digits=6, decimal_places=2)
    posX = models.DecimalField(max_digits=6, decimal_places=2)
    posY = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"Era {self.tipo} en {self.fk_lote.nombre if self.fk_lote else 'sin lote'}"


class Sensor(models.Model):
    SENSOR_TYPES = [
        ('TEM', 'Temperatura'),
        ('LUM', 'Iluminación'),
        ('HUM_A', 'Humedad Ambiental'),
        ('VIE', 'Velocidad del Viento'),
        ('HUM_T', 'Humedad del Terreno'),
        ('PH', 'Nivel de PH')
    ]

    fk_lote = models.ForeignKey(Lote, on_delete=models.SET_NULL, null=True, related_name='sensores', blank=True)
    fk_eras = models.ForeignKey(Eras, on_delete=models.SET_NULL, null=True, related_name='sensores', blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=6, choices=SENSOR_TYPES)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        tipo_sensor = dict(self.SENSOR_TYPES).get(self.tipo, 'Desconocido')
        if self.fk_eras:
            ubicacion = self.fk_eras.fk_lote.nombre
        elif self.fk_lote:
            ubicacion = self.fk_lote.nombre
        else:
            ubicacion = 'Sin ubicación'
        return f"{tipo_sensor}: {self.valor} en {ubicacion}"
