from django.shortcuts import render
from .models import Producto

def index(request):
    productos = Producto.objects.all()

    return render(request, "tienda/index.html", {
        "productos": productos
    })
