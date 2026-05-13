from django.db import models
from django.utils.text import slugify

class ModelKit(models.Model):

    nombre = models.CharField(max_length=100)
    slug=models.SlugField(blank=True)
    
    descripcion = models.TextField()
    grado = models.CharField(max_length=50)
    escala = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.IntegerField()
    
    fecha_de_ingreso = models.DateTimeField(auto_now_add=True)
    fecha_de_modificacion = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombre} - Grado: {self.grado} - Escala: {self.escala} - Precio: {self.precio} - Cantidad: {self.cantidad}"
    
