from django.shortcuts import render, get_object_or_404, redirect
from .models import zapato
from .forms import zapatoForm
from django.contrib.auth.decorators import login_required

# Pagina principal
def home(request):   
    return render(request, 'zapatillas/index.html')

# Crete/añadir zapatillas (Crud)
@login_required
def nuevo_zapato(request):
    data = {
         'form':zapatoForm()
    }

    if request.method == 'POST':
        formulario = zapatoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado correctamente"

    return render(request, 'zapatillas/zapato_nuevo.html',data)

# Read/Leer zapatillas (cRud)
def listado_zapato(request):
    Zapato = zapato.objects.all()
    data = {
        'zapatos': Zapato
    }
    return render(request, 'zapatillas/lista_zapato.html',data)

# Update/modificar zapatillas (crUd)
def modificar_zapato(request, id):
    Zapato = zapato.objects.get(id=id)
    data = {
        'form': zapatoForm(instance=Zapato)
    }

    if request.method == 'POST':
            formulario = zapatoForm(data=request.POST, instance=Zapato, files=request.FILES)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Modificado correctamente"
                data['form'] = zapatoForm(instance=zapato.objects.get(id=id))

    return render(request, 'zapatillas/modificar_zapato.html',data)

# Delete/Eliminar zapatillas (cruD)
def eliminar_zapato(request, id):
    Zapato = zapato.objects.get(id=id)
    Zapato.delete()

    return redirect(to="listado_zapato")
    
# Pagina Zapatillas por marca
def zapatos_por_marca(request, marca_id):
    zapatos = zapato.objects.filter(marca=marca_id)
    return render(request, 'zapatillas/zapatos_por_marca.html', {'zapatos': zapatos})

# Pagina de detalles de zapatillas
def detalle_zapato(request, zapato_id):
    Zapato = get_object_or_404(zapato, id=zapato_id)
    return render(request, 'zapatillas/detalle_zapato.html', {'zapato': Zapato})