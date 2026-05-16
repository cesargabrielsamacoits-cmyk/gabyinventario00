from django import forms
from .models import ActionBase

class ActionBaseForm(forms.ModelForm):

    class Meta:
        model = ActionBase
        fields = [
            'nombre',
            'descripcion',
            'precio',
            'cantidad'
        ]