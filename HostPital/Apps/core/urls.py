from django.urls import path
from Apps.core import views

urlpatterns = [
    path('',views.home, name='home'),
    path('registro/',views.registro, name='registro'),
    path('inicio/',views.index, name='inicio'),
    path('logout/',views.cerrarSesion, name='logout'),
    path('login/',views.inicioSesion, name='login'),
    
    path('inicio/perfil/',views.perfil, name='perfil'),
    path('inicio/citas/',views.cita, name='cita'),
    path('inicio/solicitarCita/',views.solicitarCita, name='solicitarCita'),
    path('inicio/pacientes/',views.pacientes, name='pacientes'),
    path('inicio/pacientes/historialclinico/<int:id>',views.historialClinico, name='historialClinico'), 
    path('inicio/historialclinico/',views.historialClinico_Cliente, name="historialClinico_cliente")
    
]
