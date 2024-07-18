

from django.urls import path
from .views import ver_carrito, añadir_al_carrito

urlpatterns = [
    path('', ver_carrito, name='ver_carrito'),
    path('añadir/', añadir_al_carrito, name='añadir_al_carrito'),
    
]




