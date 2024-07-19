
from django.urls import path
from .views import ver_carrito, añadir_al_carrito, eliminar_del_carrito, actualizar_carrito

urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('añadir/', añadir_al_carrito, name='añadir_al_carrito'),
    path('eliminar/<int:elemento_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('actualizar/<int:elemento_id>/<str:operacion>/', actualizar_carrito, name='actualizar_carrito'),
]





