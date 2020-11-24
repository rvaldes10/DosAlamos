"""Dos_Alamos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from app.views import indexOrden, login, recuperar_passwd, RegistroCliente, RegistrarOrden, RegistrarDespacho, ListarCliente, ListarOrden, ListarDespacho, publico, modificar_despacho, modificar_orden, modificar_cliente, eliminar_cliente,eliminar_despacho,eliminar_orden


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indexOrden, name="index"),
    path('login/', login, name="login"),
    path('passwd/', recuperar_passwd, name="recuperar_passwd"),
    path('registrocliente/', RegistroCliente, name="RegistroCliente"),
    path('ingresarorden/', RegistrarOrden, name="RegistrarOrden"),
    path('ingresardespacho/', RegistrarDespacho, name="RegistrarDespacho"),
    path('listadoclientes/', ListarCliente, name="ListadoClientes"),
    path('listadoordenes/', ListarOrden, name="ListadoOrdenes"),
    path('listadodespachos/', ListarDespacho, name="ListadoDespachos"),
    path('publico/',publico,name="publico"),
    path('modificar_despacho/<int:id>',modificar_despacho,name="ModificarDespacho"),
    path('modificar_orden/<int:id>',modificar_orden,name="ModificarOrden"),
    path('modificar_cliente/<int:id>',modificar_cliente,name="ModificarCliente"),
    path('eliminar_cliente/<int:id>',eliminar_cliente,name="EliminarCliente"),
    path('eliminar_orden/<int:id>',eliminar_orden,name="EliminarOrden"),
    path('eliminar_despacho/<int:id>',eliminar_despacho,name="EliminarDespacho"),
]
