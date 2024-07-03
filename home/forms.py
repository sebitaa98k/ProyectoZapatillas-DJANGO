from django import forms
from django.forms import ModelForm
from .models import zapato

class zapatoForm(ModelForm):
    class Meta:
        model = zapato
        fields = ['nombre' , 'marca' , 'precio', 'descripcion' , 'imagen']





# Hola profe si esta leyendo esto le quiero decir que en el momento
# que le estoy escribiendo esto a 20 minutos de enviar el proyecto
# se o tengo una idea de como hacer el carrito, que funciona a medias
# ya que lo hice no como deberia pero ahora como dije tengo una idea de
# como hacerlo y no alcanzare, no se lo digo para que se apiade o algo
# se lo digo porque se y podre como hacerlo, asi que esto para mi no
# se quedara asi, hare que funcione bien para minimo si lo pide para el
# examen, asi que eso. Mande info del examen pls. Buenas noches