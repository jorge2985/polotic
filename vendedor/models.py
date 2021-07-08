from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from PIL import Image
from django.db import models

# Create your models here.

class Categoria(models.Model):
    categoria   = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.categoria}"

class Producto(models.Model):
    categoria   = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="Categoria")
    titulo      = models.CharField(max_length=50)
    precio      = models.DecimalField(decimal_places=2, max_digits=10000)
    descripcion = models.TextField()
    cantidad    = models.DecimalField(decimal_places=0, max_digits=10000)
    imagen      = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    thumbnail   = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.categoria} | {self.titulo} | ${self.precio} | {self.descripcion} | {self.cantidad} | {self.imagen}"