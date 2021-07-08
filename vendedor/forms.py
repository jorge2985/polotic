from django import forms
from .models import Producto

#Formulario base que se llamara en la vista

class FormProductoCustom(forms.ModelForm):
    #campos del modelo
    class Meta:
        model = Producto
        fields = ('titulo', 'precio', 'descripcion', 'cantidad')