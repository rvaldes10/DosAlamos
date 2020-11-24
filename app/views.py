from django.shortcuts import render, redirect, get_object_or_404
from .forms import ClienteForm, Orden_CompraForm, DespachoForm
from .models import Cliente, Orden_Compra, Despacho
from django.http import Http404,HttpResponse,HttpResponseNotFound

# Create your views here.
def publico(request):
    return render(request,'publico.html')

def indexOrden(request):
    orden = Orden_Compra.objects.all()

    dataOrden = {

        'orden':orden

    }

    return render(request, 'index.html', dataOrden)

def RegistroCliente(request):

    data = {

        'form': ClienteForm()

    }

    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Cliente Registrado!"
        else:
            data["form"] = formulario

    return render(request, 'registros/cliente.html', data)

def ListarCliente(request):
    clientes = Cliente.objects.all()

    data = {

        'clientes':clientes

    }


    return render(request, 'listados/listadoclientes.html', data)

def RegistrarOrden(request):

    data = {

        'form': Orden_CompraForm()

    }

    if request.method == 'POST':
        formulario = Orden_CompraForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Orden de Compra Registrada!"
        else:
            data["form"] = formulario

    return render(request, 'registros/orden_compra.html', data)

def ListarOrden(request):
    orden = Orden_Compra.objects.all()

    data = {

        'orden':orden

    }
    return render(request, 'listados/listadoordenes.html', data)

def RegistrarDespacho(request):

    data = {

        'form': DespachoForm()

    }

    if request.method == 'POST':
        formulario = DespachoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "¡Despacho Registrado!"
        else:
            data["form"] = formulario

    return render(request, 'registros/despacho.html', data)

def ListarDespacho(request):
    despacho = Despacho.objects.all()

    data = {

        'despacho':despacho

    }

    return render(request, 'listados/listadodespachos.html', data)

def login(request):
    return render(request, 'login.html')

def recuperar_passwd(request):
    return render(request, 'password.html')

def modificar_despacho(request,id):
    despacho = get_object_or_404(Despacho,ID_Despacho=id)
    data ={
        'form' : DespachoForm(instance=despacho)
    }
    if request.method == 'POST':
        formulario = DespachoForm(data=request.POST,instance=despacho)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListadoDespachos")
        data["form"] = formulario
    return render(request,'modificacion/despacho.html',data)

def modificar_orden(request,id):
    orden = get_object_or_404(Orden_Compra,ID_Compra=id)
    data ={
        'form' : Orden_CompraForm(instance=orden)
    }
    if request.method == 'POST':
        formulario = Orden_CompraForm(data=request.POST,instance=orden)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListadoOrdenes")
        data["form"] = formulario
    return render(request,'modificacion/orden_compra.html',data)
def modificar_cliente(request,id):
    cliente = get_object_or_404(Cliente,ID_Cliente=id)
    data ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST,instance=cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="ListadoClientes")
        data["form"] = formulario
    return render(request,'modificacion/cliente.html',data)

def eliminar_cliente(request,id):
    cliente = get_object_or_404(Cliente,ID_Cliente=id)
    cliente.delete()
    return redirect(to="ListadoClientes")

def eliminar_orden(request,id):
    orden = get_object_or_404(Orden_Compra,ID_Compra=id)
    orden.delete()
    return redirect(to="ListadoOrdenes")

def eliminar_despacho(request,id):
    despacho = get_object_or_404(Despacho,ID_Despacho=id)
    despacho.delete()
    return redirect(to="ListadoDespachos")