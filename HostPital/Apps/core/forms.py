from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUsuario(UserCreationForm, forms.ModelForm):
    cc = forms.IntegerField(label='Numero de documento')
    email = forms.EmailField(label='Correo')
    telefono = forms.IntegerField(label='Numero de telefono')
    fechaNacimiento = forms.DateField(label='Fecha de nacimiento', help_text='AAAA-MM-DD')
    tipo = forms.CharField(initial='cliente')
    password1 = forms.CharField(label='Contraseña',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña',widget=forms.PasswordInput)
    
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','cc','email','telefono','fechaNacimiento','password1','password2']
        help_text = {k:"" for k in fields}
        
    def __init__(self, *args, **kwargs):
        super(RegistroUsuario, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget = forms.HiddenInput()
        self.fields['tipo'].initial = 'cliente'