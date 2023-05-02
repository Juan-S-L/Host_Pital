from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.urls import reverse

from .forms import RegistroUsuario
from Apps.medios_internos.forms import CitaForm, HistorialForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from Apps.core.models import User
from Apps.medios_internos.models import Cita, HistorialCliente

from datetime import datetime, timedelta

from django.db import IntegrityError


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
                nombre = request.POST['first_name']
                apellido = request.POST['last_name']
                username = nombre.split(' ')[1].lower() + '.' + apellido.split(' ')[0].lower()
                user = User.objects.create_user(
                    username=username,
                    first_name=request.POST['first_name'],
                    last_name=request.POST['last_name'],
                    cc=request.POST['cc'],
                    email=request.POST['email'],
                    telefono=request.POST['telefono'],
                    fechaNacimiento=request.POST['fechaNacimiento'],
                    password=request.POST['password1'],
                    tipo=request.POST['tipo'],
                    sexo=request.POST['sexo'],
                    direccionResidencia=request.POST['direccionResidencia'],
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


def solicitarCita(request):
    if request.method == 'GET':
        return render(request, 'solicitarCita.html',{
            'form': CitaForm
        })
    else:
        form = CitaForm(request.POST)
        if form.is_valid():
            hora = form.cleaned_data['hora']
            doctor = form.cleaned_data['user_doctor']
            fechaHora_I = datetime.now() + timedelta(days=3, hours=hora.hour, minutes=hora.minute)
            fechaHora_F = fechaHora_I + timedelta(minutes=20)
            cita = Cita(user_doctor=doctor, user_cliente=request.user, fechaHora_I=fechaHora_I, fechaHora_F=fechaHora_F)
            cita.save()
            # messages.success(request, 'La cita a sido creada exitosamente')
            return redirect('inicio')


def perfil(request):
    return render(request, 'perfil.html')


def pacientes(request):
    doctor = request.user
    citas = Cita.objects.filter(user_doctor=doctor)
    
    paciente = set()
    for cita in citas:
        paciente.add(cita.user_cliente)
    
    if request.method == 'POST':
        idPaciente = request.POST.get('paciente_id')
        # print(idPaciente)
        url = reverse('historialClinico', args=[idPaciente])
        return redirect(url)
    
    return render(request, 'pacientes.html',{
        'pacientes':paciente,
    })


def historialClinico(request,id):
    cliente = User.objects.get(id=id)
    try:
        historial = HistorialCliente.objects.get(user_clinte=cliente)
    except HistorialCliente.DoesNotExist:
        historial = HistorialCliente(user_clinte=cliente,user_doctor=request.user)
        historial.save()
        
    if request.method == 'POST':
        form = HistorialForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = HistorialForm(instance=historial)
    
    return render(request, 'historialclinico.html',{
        'form':form,
        'cliente':cliente,
    })
    

def historialClinico_Cliente(request):
    historial = HistorialCliente.objects.get(user_clinte=request.user)
    return render(request, 'historialClinico_Cliente.html',{
        'historial':historial
    })