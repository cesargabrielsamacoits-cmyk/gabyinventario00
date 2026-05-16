from django.db import models
from django.utils.text import slugify


class BaseModel(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    slug = models.SlugField(unique=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre)
        super().save(*args, **kwargs)


class ActionBase(BaseModel):

    TAMAÑOS = [
        ("AB1", "Action Base 1"),
        ("AB2", "Action Base 2"),
        ("AB4", "Action Base 4"),
        ("AB5", "Action Base 5"),
    ]

    tipo = models.CharField(max_length=10, choices=TAMAÑOS)

    def __str__(self):
        return self.nombre