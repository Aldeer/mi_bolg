from django.db.models import Model
from django.db.models import AutoField
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import DateField
from django.db.models import URLField
from django.db.models import EmailField
from django.db.models import ForeignKey
from ckeditor.fields import RichTextField
from django.db.models import CASCADE


# Create your models here.
class Categoria(Model):
    id = AutoField(primary_key=True)
    nombre = CharField(
        "Nombre de la categoria", 
        max_length=100, 
        blank=False, 
        null=False
    )
    estado = BooleanField(
        "Categoria Activada/Categoria Desactivada",
        default=True
    )
    fecha_creacion = DateField(
        "Fecha de creacion",
        auto_now=False,
        auto_now_add=True
    )


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre
    

class Autor(Model):
    id = AutoField(primary_key=True)
    nombres = CharField(
        'Nombres de autor',
        max_length=255,
        blank=False,
        null=False
    )
    apellidos = CharField(
        'Apellidos de autor',
        max_length=255,
        blank=False,
        null=False
    )
    facebook = URLField(
        'Facebook',
        blank=True,
        null=True
    )
    instagram = URLField(
        'Instagram',
        blank=True,
        null=True
    )
    twitter = URLField(
        'Twitter',
        blank=True,
        null=True
    )
    pagina_web = URLField(
        'Pagina web',
        blank=True,
        null=False
    )
    correo = EmailField(
        'Correo electronico',
        blank=False,
        null=False
    )
    estado = BooleanField(
        'Autor Activo/Inactivo',
        default=True
    )
    fecha_creacion = DateField(
        'Fecha de creacion',
        auto_now=False,
        auto_now_add=True
    )


    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return '{0}, {1}'.format(self.apellidos, self.nombres)
    

class Post(Model):
    id = AutoField(primary_key=True)
    titulo = CharField('Titulo', max_length=90, blank=False, null=False)
    slug = CharField('Slug', max_length=100 ,blank=False, null=False)
    descripcion = CharField('Descripcion', max_length=110, blank=False, null=False)
    contenido = RichTextField()
    imagen = URLField('URL imagen', max_length=255, blank=False, null=False)
    autor = ForeignKey(Autor, on_delete=CASCADE)
    categoria = ForeignKey(Categoria, on_delete=CASCADE)
    estado = BooleanField('Publicado/No Publicado', default=True)
    fecha_creacion = DateField('Fecha de creacion', auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo