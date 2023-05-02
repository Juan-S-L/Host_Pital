from django.db import models
from Apps.core.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.

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
    user_doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Doctor',null=True, blank=True,limit_choices_to={'tipo':'doctor'}, related_name='doctores_especilistas')
    espcialidad = models.CharField(max_length=68, choices=TIPOS_DE_MEDICOS, verbose_name='Especialidad',null=True, blank=True)
    
    @property
    def doctor(self):
        return f'{self.user_doctor.first_name} {self.user_doctor.last_name}'
    
    class Meta():
        verbose_name = 'Dr. con especialidad'
        verbose_name_plural = 'Dr. con especialidades'

class Cita(models.Model):
    user_doctor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Doctor',limit_choices_to={'tipo':'doctor'}, related_name='citas_doctor')
    user_cliente = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='Cliente',limit_choices_to={'tipo':'cliente'}, related_name='citas_cliente')
    fechaHora_I = models.DateTimeField(null=True, verbose_name='Fecha y hora de inicio')
    fechaHora_F = models.DateTimeField(null=True, verbose_name='Fecha y hora de cierre')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.fechaHora_F = self.fechaHora_I + timedelta(minutes=20)
        else:
            citaAnte = Cita.objects.get(id=self.id)
            if citaAnte.fechaHora_I !=  self.fechaHora_I:
                self.fechaHora_F = self.fechaHora_I + timedelta(minutes=20)
                
        super().save(*args, **kwargs)
    
    @property
    def cliente(self):
        return f'{self.user_cliente.first_name} {self.user_cliente.last_name}'
    
    @property
    def doctor(self):
        return f'{self.user_doctor.first_name} {self.user_doctor.last_name}'
    
class HistorialCliente(models.Model):
    user_clinte = models.ForeignKey(User,null=True,on_delete=models.CASCADE,verbose_name='Cliente',limit_choices_to={'tipo':'cliente'}, related_name='historial_cliente')
    user_doctor = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='Doctor',limit_choices_to={'tipo':'doctor'}, related_name='historial_doctor')
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_actualizacion = models.DateTimeField(auto_now=True,verbose_name='Actualización')
    
    enfermedades_previas = models.TextField(blank=True, null=True,verbose_name='Enfermedades')
    medicamentos = models.TextField(blank=True, null=True,verbose_name='Medicamentos')
    alergias = models.TextField(blank=True, null=True,verbose_name='Alergias')
    examenes_realizados = models.TextField(blank=True, null=True,verbose_name='Examenes realizados')
    
    @property
    def cliente(self):
        return f'{self.user_clinte.first_name} {self.user_clinte.last_name}' if self.user_clinte else ''
    
    @property
    def doctor(self):
        return f'{self.user_doctor.first_name} {self.user_doctor.last_name}'