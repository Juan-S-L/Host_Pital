from django.contrib import admin
from Apps.medios_internos.models import DoctorEsp, Cita
# Register your models here.

@admin.register(DoctorEsp)
class DocEsp(admin.ModelAdmin):
    list_display = ('id','doctor','espcialidad')
    list_filter = ('espcialidad',)
    search_fields = ('id', 'espcialidad')
    
@admin.register(Cita)
class cita_(admin.ModelAdmin):
    list_display = ('id','doctor','cliente','fechaHora_I','fechaHora_F')
