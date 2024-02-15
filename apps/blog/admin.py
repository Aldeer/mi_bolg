from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from .models import Autor
from .models import Categoria
from .models import Post

class CategoriaAdmin(ModelAdmin):
    # activa la barra de busqueda
    # se le pasa una lista con los campos por los que vamos 
    # a realizar la busquerda
    search_fields = ['nombre']

    # 
    list_display = ['nombre', 'estado', 'fecha_creacion']

class AutorAdmin(ModelAdmin):
    search_fields = ['nombres', 'apellidos', 'correo']
    list_display = ['nombres', 'apellidos', 'correo', 'estado', 'fecha_creacion']

    
# Register your models here.
site.register(Autor, AutorAdmin)
site.register(Categoria, CategoriaAdmin)
site.register(Post)
