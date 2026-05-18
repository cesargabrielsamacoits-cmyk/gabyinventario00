from django.db import models
from django.contrib.auth.models import User 

class InfoExtraUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.telefono}"
