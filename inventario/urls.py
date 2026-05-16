from django.urls import path
from inventario.views import *

urlpatterns = [
    path('', index, name='index'),
    path('modelkits/', modelkit_list, name='modelkit_list'),
    path('modelkits/agregar/', agregar_modelkit, name='agregar_modelkit'),
    path('modelkits/list/', ModelKitListView.as_view(), name='modelkit_list_view'),
    path('modelkits/<slug:slug>/', ModelKitDetailView.as_view(), name='modelkit_detail_view'),
    path(
    'modelkits/<slug:slug>/editar/',
    ModelKitUpdateView.as_view(),
    name='modelkit_update_view',
),
    path(
    'modelkits/<slug:slug>/eliminar/',
    ModelKitDeleteView.as_view(),
    name='modelkit_delete_view',
),
]


