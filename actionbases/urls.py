from django.urls import path

from .views import (
    base_list,
    base_create,
    ActionBaseDetailView,
    ActionBaseUpdateView,
    ActionBaseDeleteView
)

urlpatterns = [

    path('', base_list, name='base_list'),

    path(
        'create/',
        base_create,
        name='base_create'
    ),

    path(
        '<slug:slug>/',
        ActionBaseDetailView.as_view(),
        name='base_detail_view'
    ),

    path(
        '<slug:slug>/editar/',
        ActionBaseUpdateView.as_view(),
        name='base_update_view'
    ),

    path(
        '<slug:slug>/eliminar/',
        ActionBaseDeleteView.as_view(),
        name='base_delete_view'
    ),

]