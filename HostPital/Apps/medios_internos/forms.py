from django import forms
from .models import Cita, InfoCliente
from Apps.core.models import User

class CitaForm(forms.ModelForm):
    hora = forms.TimeField(label='Hora de la cita')

    class Meta:
        model = Cita
        fields = ['user_doctor','hora',]
        
class InfoCliente(forms.ModelForm):
    sexo = forms.ChoiceField(label='Genero', choices=InfoCliente.tipoSexo, initial='M')
    direccionResidencia = forms.CharField(label='Direccion de residencia', max_length=80)
    nacionalidad = forms.CharField(label='Nacionalidad', max_length=80)
    
    class Meta:
        model = InfoCliente
        fields = ['sexo','direccionResidencia','nacionalidad']