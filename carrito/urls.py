

from django.urls import path
from .views import ver_carrito, añadir_al_carrito, eliminar_del_carrito, actualizar_cantidad

urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('añadir/', añadir_al_carrito, name='añadir_al_carrito'),
    path('eliminar/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar/', actualizar_cantidad, name='actualizar_cantidad'),
]






