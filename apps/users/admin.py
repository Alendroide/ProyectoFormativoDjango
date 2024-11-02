from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario
from api.forms import UsuarioCreationForm

class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm
    model = Usuario
    list_display = ['correoElectronico', 'identificacion', 'nombre', 'apellidos', 'telefono', 'admin']
    fieldsets = (
        (None, {'fields': ('correoElectronico', 'identificacion', 'nombre', 'apellidos', 'fechaNacimiento', 'telefono', 'admin')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('correoElectronico', 'identificacion', 'nombre', 'apellidos', 'fechaNacimiento', 'telefono', 'admin', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('correoElectronico',)

admin.site.register(Usuario, UsuarioAdmin)