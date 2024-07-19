from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrito, ElementoCarrito
from home.models import zapato
from django.contrib.auth.decorators import login_required

@login_required
def ver_carrito(request):
    carrito = Carrito.objects.first()
    if not carrito:
        carrito = Carrito.objects.create()
    elementos = ElementoCarrito.objects.filter(carrito=carrito)
    total = carrito.calcular_total()
    return render(request, 'carrito/ver_carrito.html', {'carrito': carrito, 'elementos': elementos, 'total': total})

@login_required
def añadir_al_carrito(request):
    if request.method == 'POST':
        zapato_id = request.POST.get('zapato_id')
        cantidad = request.POST.get('cantidad', 1)
        zapato_obj = get_object_or_404(zapato, id=zapato_id)
        carrito = Carrito.objects.first()
        if not carrito:
            carrito = Carrito.objects.create()
        elemento, created = ElementoCarrito.objects.get_or_create(carrito=carrito, zapato=zapato_obj)
        if not created:
            elemento.cantidad += int(cantidad)
        else:
            elemento.cantidad = int(cantidad)
        elemento.save()
        return redirect('ver_carrito')
    return redirect('home')

@login_required
def eliminar_del_carrito(request, elemento_id):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    elemento.delete()
    return redirect('ver_carrito')

@login_required
def actualizar_carrito(request, elemento_id, operacion):
    elemento = get_object_or_404(ElementoCarrito, id=elemento_id)
    if operacion == 'sumar':
        elemento.cantidad += 1
    elif operacion == 'restar' and elemento.cantidad > 1:
        elemento.cantidad -= 1
    elemento.save()
    return redirect('ver_carrito')





