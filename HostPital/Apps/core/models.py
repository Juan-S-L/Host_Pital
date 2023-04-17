from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class User(AbstractUser):
    tipoUsuario = (
        ('doctor', 'Doctor'),
        ('enfermero', 'Enfermero'),
        ('cliente', 'Cliente'),
    )
    cc = models.IntegerField(null=True, blank=True,verbose_name='Numero de documento')
    telefono = models.PositiveIntegerField(help_text=('+ 57'), null=True, blank=True)
    fechaNacimiento = models.DateField(help_text=('AAAA-MM-DD'),null=True, blank=True,verbose_name='Fecha nacimiento')
    tipo = models.CharField(max_length=58, null=True, blank=True, choices=tipoUsuario,verbose_name='Tipo de usuario')