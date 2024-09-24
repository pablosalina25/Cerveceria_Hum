from django.contrib import admin
from cerveceria.models import Cerveza, Fabricante,Presentacion

# Register your models here.

class FabricanteAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais','sitio_web','email')
    search_fields = ('nombre','pais')
    list_filter = ('nombre','pais','sitio_web','email')

class CervezaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fabricante','presentacion')
    search_fields = ('nombre','fabricante')
    list_filter = ('fabricante','presentacion','origen')
    ordering = ('fecha_elaboracion',)
    date_hierarchy = ('fecha_elaboracion')

class PresentacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','tamaño')
    search_fields = ('nombre','tamaño')
    list_filter = ('nombre','tamaño')

admin.site.register(Cerveza,CervezaAdmin)
admin.site.register(Fabricante,FabricanteAdmin)
admin.site.register(Presentacion,PresentacionAdmin)