from django.urls import path
from .views import iniciar_sesion, cerrar_sesion , registro , perfil, CambiarContrasenaView
#from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('cerrar-sesion/', cerrar_sesion, name='cerrar_sesion'),
    path('registro/', registro, name='registro'),
    path('perfil/', perfil, name='perfil'),
    path(
    'cambiar-contrasena/',
    CambiarContrasenaView.as_view(),
    name='cambiar_contrasena'
),
]
