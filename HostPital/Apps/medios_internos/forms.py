from django import forms
from .models import Cita
from Apps.core.models import User

class CitaForm(forms.ModelForm):
    hora = forms.TimeField(label='Hora de la cita')

    class Meta:
        model = Cita
        fields = ['user_doctor','hora',]