from django.urls import path
from inicio.views import inicio , bienvenida , fecha , template1

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('bienvenida/', bienvenida, name='bienvenida'),
    path('fecha/', fecha, name='fecha'),
    path('template1/', template1, name='template1'),
]
