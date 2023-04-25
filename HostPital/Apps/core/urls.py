from django.urls import path
from Apps.core import views

urlpatterns = [
    path('',views.home, name='home'),
    path('registro/',views.registro, name='registro'),
    path('inicio/',views.index, name='inicio'),
    path('logout/',views.cerrarSesion, name='logout'),
    path('inicio/perfil/',views.perfil, name='perfil'),
    path('login/',views.inicioSesion, name='login'),
    
    path('inicio/citas/',views.cita, name='cita'),
    path('inicio/solicitarCita/',views.solicitarCita, name='solicitarCita'),
    
    
]
