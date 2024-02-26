from .Carro import Carro
from django.shortcuts import redirect, reverse
from tienda.models import Producto
from urllib.parse import urlencode

def agregar_carro(request, pk):

    if request.user.is_authenticated:
        carro = Carro(request)
        producto = Producto.objects.filter(pk=pk).first()
        carro.agregar(producto=producto)

        return redirect("tienda")

    return redirect(reverse('tienda')+"?error='not auth'")

def restar_producto(request, pk):
    if request.user.is_authenticated:
        carro = Carro(request)
        producto = Producto.objects.filter(pk=pk).first()
        carro.restar_producto(producto=producto)

        return redirect("tienda")
    return redirect("tienda")

def eliminar_carro(request, pk):
    if request.user.is_authenticated:
        carro = Carro(request)
        producto = Producto.objects.filter(pk=pk).first()
        carro.eliminar(producto=producto)

        return redirect("tienda")
    return redirect("tienda")

def limpiar_carro(request):
    if request.user.is_authenticated:
        carro = Carro(request)
        carro.limpiar_carro()

        return redirect("tienda")

    return redirect("tienda")
