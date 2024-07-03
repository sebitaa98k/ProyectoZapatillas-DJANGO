from django import forms
from django.forms import ModelForm
from .models import zapato

class zapatoForm(ModelForm):
    class Meta:
        model = zapato
        fields = ['nombre' , 'marca' , 'precio', 'descripcion' , 'imagen']