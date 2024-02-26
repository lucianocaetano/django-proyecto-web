from django.shortcuts import render, HttpResponse
from carrito.Carro import Carro
#home views

def index(request):

    carro = Carro(request)
    return render(request, "ProyectoWebApp/index.html")


