from django.db import models



# Modelo zapatilla
class zapato(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre  = models.CharField(max_length=100)
    marca = models.IntegerField(choices=[
        (1,'Adidas'),
        (2,'Converse'),
        (3,'Nike'),
    ], default=1)
    imagen = models.ImageField(upload_to='zapatos/', null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField(default=0)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre