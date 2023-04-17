from django.contrib import admin
from Apps.medios_internos.models import DoctorEsp, cita
# Register your models here.

@admin.register(DoctorEsp)
class DocEsp(admin.ModelAdmin):
    list_display = ('id','doctor','espcialidad')
    list_filter = ('espcialidad',)
    search_fields = ('id', 'espcialidad')
    
@admin.register(cita)
class cita_(admin.ModelAdmin):
    list_display = ('id','doctor','cliente','fechaHora')
