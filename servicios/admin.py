from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Solicitud)
admin.site.register(UsuarioCategoria)

@admin.register(Categoria)
class Categoria(admin.ModelAdmin):
	list_display = ('nombre', 'tipo', 'padre')
	list_filter = ('tipo', 'padre')
