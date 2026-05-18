from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import InfoExtraUser

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class FormularioCambioContrasena(PasswordChangeForm):

    old_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    new_password1 = forms.CharField(
        label='Nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    new_password2 = forms.CharField(
        label='Confirmar nueva contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class FormularioEdicionPerfil(UserChangeForm):

    password = None
    telefono = forms.CharField(label='Teléfono', max_length=20, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    direccion = forms.CharField(label='Dirección', max_length=255, required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'telefono', 'direccion']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        if user:
            perfil, created = InfoExtraUser.objects.get_or_create(user=user)
            self.fields['telefono'].initial = perfil.telefono
            self.fields['direccion'].initial = perfil.direccion

    def save(self, commit=True):

        user = super().save(commit)

        perfil, created = InfoExtraUser.objects.get_or_create(user=user)

        perfil.telefono = self.cleaned_data['telefono']
        perfil.direccion = self.cleaned_data['direccion']

        if commit:
            perfil.save()

        return user