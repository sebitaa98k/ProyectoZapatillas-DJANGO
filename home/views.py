from django.shortcuts import render
from .models import zapato


def home(request):
    zapatos = zapato.objects.all()

    query = request.GET.get('q')
    if query:
        zapatos = zapatos.filter(nombre__icontains=query)

    return render(request, 'zapatillas/index.html', {'zapatos':zapatos})


