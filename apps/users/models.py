from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    username = None
    identificacion = models.BigIntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correoElectronico = models.EmailField(max_length=255, unique=True)
    admin = models.BooleanField(default=False, null=False)

    USERNAME_FIELD = 'correoElectronico'
    REQUIRED_FIELDS = ['identificacion', 'nombre', 'apellidos', 'fechaNacimiento', 'telefono']

    def __str__(self):
        return str(self.identificacion)