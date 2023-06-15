from django.db import models

# Create your models here.
from django.db import models

class Capacitacion(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

class Suscripcion(models.Model):
    email = models.EmailField()
    fecha_registro = models.DateField(auto_now_add=True)

