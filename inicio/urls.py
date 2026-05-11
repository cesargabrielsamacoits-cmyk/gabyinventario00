from django.urls import path
from inicio.views import inicio , bienvenida , fecha 

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('fecha/', fecha, name='fecha'),
]
