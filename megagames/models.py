from django.db import models
from django.core.exceptions import ValidationError

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=100)
    descripcion = models.TextField("Descripción")
    precio = models.IntegerField("Precio")
    consolas = models.CharField("Consolas", max_length=100)
    stock = models.IntegerField("Stock")
    imagen = models.ImageField("Imagen", upload_to='imagenes/', null=True, blank=True)
    url_imagen = models.URLField("URL de la Imagen", max_length=200, null=True, blank=True)

    def clean(self):
        if not self.imagen and not self.url_imagen:
            raise ValidationError('Debe proporcionar una imagen o una URL de la imagen.')

    def __str__(self):
        return self.nombre

class Consola(models.Model):
    idconsola = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.IntegerField("Precio")
    stock = models.IntegerField("Stock")
    imagen = models.ImageField("Imagen", upload_to='imagenes/', null=True, blank=True)
    url_imagen = models.URLField("URL de la Imagen", max_length=200, null=True, blank=True)

    def clean(self):
        if not self.imagen and not self.url_imagen:
            raise ValidationError('Debe proporcionar una imagen o una URL de la imagen.')

    def __str__(self):
        return self.nombre
    
class Jugete(models.Model):
    idjugete = models.AutoField(primary_key=True)
    nombre = models.CharField("Nombre", max_length=100)
    precio = models.IntegerField("Precio")
    stock = models.IntegerField("Stock")
    imagen = models.ImageField("Imagen", upload_to='imagenes/', null=True, blank=True)
    url_imagen = models.URLField("URL de la Imagen", max_length=200, null=True, blank=True)

    def clean(self):
        if not self.imagen and not self.url_imagen:
            raise ValidationError('Debe proporcionar una imagen o una URL de la imagen.')

    def __str__(self):
        return self.nombre