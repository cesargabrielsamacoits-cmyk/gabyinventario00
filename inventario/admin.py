from django.contrib import admin
#from .models import ModelKit
from inventario.models import ModelKit  
from actionbases.models import ActionBase

#admin.site.register(ModelKit)

@admin.register(ModelKit)
class ModelKitAdmin(admin.ModelAdmin):
    #columnas a mostrar en la lista de objetos del panel de administración
    list_display = ('nombre', 'grado', 'escala', 'precio', 'cantidad', 'fecha_de_ingreso', 'fecha_de_modificacion')
   
    search_fields = ('nombre', 'grado', 'escala')
   
    list_filter = ('grado', 'escala')
    
    ordering = ('nombre', 'grado', 'escala')
    
    readonly_fields = ('fecha_de_ingreso', 'fecha_de_modificacion')
    
@admin.register(ActionBase)
class ActionBaseAdmin(admin.ModelAdmin):
    ordering = ['nombre']
    list_display = ['nombre', 'slug']
    list_filter = ['nombre']