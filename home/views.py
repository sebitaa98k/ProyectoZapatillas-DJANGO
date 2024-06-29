from django.shortcuts import render, get_object_or_404
from .models import zapato


def home(request):
    zapatos = zapato.objects.all()

    query = request.GET.get('q')
    if query:
        zapatos = zapatos.filter(nombre__icontains=query)

    return render(request, 'zapatillas/index.html', {'zapatos':zapatos})


def zapatos_por_marca(request, marca_id):
    zapatos = zapato.objects.filter(marca=marca_id)
    return render(request, 'zapatillas/zapatos_por_marca.html', {'zapatos': zapatos})


def detalle_zapato(request, zapato_id):
    Zapato = get_object_or_404(zapato, id=zapato_id)
    return render(request, 'zapatillas/detalle_zapato.html', {'zapato': Zapato})