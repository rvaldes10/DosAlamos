from django import forms
from .models import Cliente, Orden_Compra, Despacho

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'

class Orden_CompraForm(forms.ModelForm):

    class Meta:
        model = Orden_Compra
        fields = '__all__'

        widgets = {

            "Fecha_Emision":forms.SelectDateWidget()

        }

class DespachoForm(forms.ModelForm):

    class Meta:
        model = Despacho
        fields = '__all__'

    widgets = {

            "Fecha_Emision":forms.SelectDateWidget()

        }