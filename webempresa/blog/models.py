from django.db import models
from django.utils.timezone import now

# USUARIOS REGISTRADOS EN DJANGO
from django.contrib.auth.models import User


# Create your models here.
class Category (models.Model):
    name = models.CharField( max_length=100, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'
        ordering = ['-created']
    def __str__(self) -> str:
        return self.name

class Post (models.Model):
    title =models.CharField( max_length=200, verbose_name='Título')
    content = models.TextField(verbose_name = 'Contenido')
    published = models.DateTimeField(verbose_name=' Fecha de publicación', default=now)
    image = models.ImageField(verbose_name='Imagen', upload_to = 'Blog', null=True, blank = True)
    # CLAVE FORANEA (USUARIO -> POST )
    # on_delete= models.CASCADE => BORRADO EN CASCADA
    author = models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE)
    # CLAVE FORANEA (CATEGORY -> POST ) MANY TO MANY | related_name => sirve para ponerle un tag a la hora de hacer la consulta (category->post)
    categories = models.ManyToManyField(Category, verbose_name='Categorías', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')

    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'
        ordering = ['-created']
    def __str__(self) -> str:
        return self.title
