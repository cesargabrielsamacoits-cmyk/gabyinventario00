from django import forms
from inventario.models import ModelKit

class ModelKitForm(forms.ModelForm):
    class Meta:
        model = ModelKit
        fields = ['nombre', 'descripcion', 'grado', 'escala', 'precio', 'cantidad']