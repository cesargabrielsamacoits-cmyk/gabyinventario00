from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import login, logout
from .forms import FormularioRegistro , FormularioCambioContrasena
from django.urls import reverse_lazy

def iniciar_sesion(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            user=formulario.get_user()
            
            login(request,  user)
            # Aquí puedes agregar la lógica para iniciar sesión al usuario
            return redirect('index')  # Redirige a la lista de ModelKits después de iniciar sesión
    else:
        formulario = AuthenticationForm(request)
    
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario': formulario})

def cerrar_sesion(request):

    if request.method == "POST":
        logout(request)
        return redirect('index')

    return render(
        request,
        "usuarios/cerrar_sesion.html"
    )


def registro(request):
    if request.method == 'POST':
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:iniciar_sesion') # Redirige a la página de inicio de sesión después de registrarse
        else:
            return render(request, 'usuarios/registro.html', {'formulario': formulario})
    return render(request, 'usuarios/registro.html', {'formulario': FormularioRegistro()})


def perfil(request):
    return render(request, 'usuarios/perfil.html')


class CambiarContrasenaView(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasena.html'
    success_url = reverse_lazy('usuarios:perfil')
    form_class = FormularioCambioContrasena