from django.shortcuts import render, redirect

from .forms import RegistroUsuario

from django.contrib.auth.forms import AuthenticationForm
from Apps.core.models import User
from django.contrib.auth import login, logout, authenticate

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
