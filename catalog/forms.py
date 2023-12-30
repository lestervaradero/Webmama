from django import forms
from .models import Producto


class NombreForm(forms.Form):
    NombreProd = forms.CharField(label="Nombre", max_length=100)