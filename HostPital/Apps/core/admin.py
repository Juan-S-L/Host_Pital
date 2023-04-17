from django.contrib import admin
from Apps.core.models import User
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id','tipo','username','first_name','last_name','email','cc','is_active')
    list_filter = ('tipo','is_active',)
    search_fields = ('id','tipo','first_name','last_name','cc')