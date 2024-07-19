from django.db import models
from home.models import zapato

class Carrito(models.Model):
    def calcular_total(self):
        total = sum(elemento.precio_total for elemento in self.elementocarrito_set.all())
        return total

class ElementoCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    zapato = models.ForeignKey(zapato, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.precio_total = self.cantidad * self.zapato.precio
        super().save(*args, **kwargs)

