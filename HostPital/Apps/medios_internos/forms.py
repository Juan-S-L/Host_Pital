from django import forms
from .models import Cita, HistorialCliente
from Apps.core.models import User

class CitaForm(forms.ModelForm):
    hora = forms.TimeField(label='Hora de la cita')

    class Meta:
        model = Cita
        fields = ['user_doctor','hora',]
        
class HistorialForm(forms.ModelForm):
    class Meta:
        model = HistorialCliente
        fields = ('enfermedades_previas', 'medicamentos', 'alergias', 'examenes_realizados')
        widgets = {
            'enfermedades_previas': forms.Textarea(attrs={'rows': 3}),
            'medicamentos': forms.Textarea(attrs={'rows': 3}),
            'alergias': forms.Textarea(attrs={'rows': 3}),
            'examenes_realizados': forms.Textarea(attrs={'rows': 3}),
        }