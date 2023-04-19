from django.shortcuts import render, redirect
from django.http import JsonResponse

from .forms import RegistroUsuario

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate

from Apps.core.models import User
from Apps.medios_internos.models import Cita

from django.db import IntegrityError

# Create your views here.


def home(request):
    return render(request, 'home.html')


def registro(request):
    if request.method == 'GET':
        return render(request, 'register.html', {
            'form': RegistroUsuario
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    cc=request.POST['cc'],
                    email=request.POST['email'],
                    telefono=request.POST['telefono'],
                    fechaNacimiento=request.POST['fechaNacimiento'],
                    password=request.POST['password1'],
                    tipo=request.POST['tipo']
                )
                user.save()
                login(request, user)
                return redirect('inicio')
            except IntegrityError:
                return render(request, 'register.html', {
                    'form': RegistroUsuario,
                    'msg': 'Usuario ya existe'
                })

        return render(request, 'register.html', {
            'form': RegistroUsuario,
            'msg': 'La contraseña no es la misma'
        })


def index(request):
    return render(request, 'index.html')


def cerrarSesion(request):
    logout(request)
    return redirect('home')


def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'singin.html', {
                'form': AuthenticationForm,
                'msg': 'Usuario o contraseña invalidos'
            })
        else:
            login(request, user)
            return redirect('inicio')

def cita(request):
    
    if request.user.tipo == 'doctor':   
        citas = Cita.objects.filter(user_doctor=request.user)
    else:
        citas = Cita.objects.filter(user_cliente=request.user)
    citas_dict = []
    for cita in citas:
        cita_dict = {
            'title': f'{cita.doctor} - {cita.cliente}',
            'start': cita.fechaHora_I.isoformat(),
            'end': cita.fechaHora_F.isoformat(),
            'id': cita.id,  # aquí debes especificar un valor para el parámetro 'id'
        }
        citas_dict.append(cita_dict)

    return render(request, 'citas.html',{
        'citas': citas_dict,
    })