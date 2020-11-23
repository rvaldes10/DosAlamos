from django.shortcuts import render
from .forms import ClienteForm, Orden_CompraForm, DespachoForm
from .models import Cliente, Orden_Compra, Despacho

# Create your views here.

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
