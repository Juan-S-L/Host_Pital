from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm, forms.ModelForm):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro')
    )
    
    cc = forms.IntegerField(label='Numero de documento')
    email = forms.EmailField(label='Correo')
    telefono = forms.IntegerField(label='Numero de telefono')
    fechaNacimiento = forms.DateField(label='Fecha de nacimiento', help_text='AAAA-MM-DD')
    tipo = forms.CharField(initial='cliente')
    
    sexo = forms.ChoiceField(label='Genero', choices=SEXO_CHOICES, initial='M')
    direccionResidencia = forms.CharField(label='Direccion de residencia', max_length=80)
    
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña',widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['tipo'].initial = 'cliente'
    
    class Meta:
        model = User
        fields = ['first_name','last_name','cc','email','telefono','fechaNacimiento','sexo','direccionResidencia','password1','password2']
        help_text = {k:"" for k in fields}