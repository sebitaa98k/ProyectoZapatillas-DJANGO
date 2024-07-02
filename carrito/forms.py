from django import forms

class AñadirAlCarritoForm(forms.Form):
    zapato_id = forms.IntegerField()
    cantidad = forms.IntegerField()

class EliminarDelCarritoForm(forms.Form):
    elemento_id = forms.IntegerField()


