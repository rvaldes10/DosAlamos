from django.contrib import admin
from .models import Orden_Compra, Cliente, Despacho

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Orden_Compra)
admin.site.register(Despacho)