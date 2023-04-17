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
    
class DoctorEsp(models.Model):
    TIPOS_DE_MEDICOS = (
        ('anestesiologo', 'Anestesiólogo'),
        ('cardiologo', 'Cardiólogo'),
        ('cirujano', 'Cirujano'),
        ('dermatologo', 'Dermatólogo'),
        ('endocrinologo', 'Endocrinólogo'),
        ('gastroenterologo', 'Gastroenterólogo'),
        ('ginecologo', 'Ginecólogo'),
        ('hematologo', 'Hematólogo'),
        ('infectologo', 'Infectólogo'),
        ('internista', 'Internista'),
        ('nefrologo', 'Nefrólogo'),
        ('neurologo', 'Neurólogo'),
        ('oftalmologo', 'Oftalmólogo'),
        ('oncologo', 'Oncólogo'),
        ('otorrinolaringologo', 'Otorrinolaringólogo'),
        ('patologo', 'Patólogo'),
        ('pediatra', 'Pediatra'),
        ('psiquiatra', 'Psiquiatra'),
        ('radiologo', 'Radiólogo'),
        ('reumatologo', 'Reumatólogo'),
        ('traumatologo', 'Traumatólogo'),
        ('general', 'Médico General'),
    )
    user_doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Doctor',null=True, blank=True,limit_choices_to={'tipo':'doctor'})
    espcialidad = models.CharField(max_length=68, choices=TIPOS_DE_MEDICOS, verbose_name='Especialidad',null=True, blank=True)
    
    @property
    def doctor(self):
        return f'{self.user_doctor.first_name} {self.user_doctor.last_name}'
    
    class Meta():
        verbose_name = 'Dr. con especialidad'
        verbose_name_plural = 'Dr. con especialidades'

    