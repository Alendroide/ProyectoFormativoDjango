from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, identificacion, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        if not identificacion:
            raise ValueError("El usuario debe tener una identificación")
        
        email = self.normalize_email(email)
        user = self.model(email=email, identificacion=identificacion, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, identificacion, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(email, identificacion, password, **extra_fields)

class Usuario(AbstractUser):
    username = None
    identificacion = models.BigIntegerField(unique=True, null=False)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    fechaNacimiento = models.DateField()
    telefono = models.CharField(max_length=15)
    correoElectronico = models.CharField(max_length=20,unique=True,null=False)
    admin = models.BooleanField(default=False, null=False)

    USERNAME_FIELD = 'correoElectronico'
    REQUIRED_FIELDS = ['identificacion', 'nombre', 'apellidos', 'fechaNacimiento', 'telefono']

    objects = UsuarioManager()

    def __str__(self):
        return str(self.identificacion)
