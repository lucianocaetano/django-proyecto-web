from django.shortcuts import render
from .models import Servicios
#servicios views
def index(request):
    servicios = Servicios.objects.all()

    return render(request, "servicios/index.html", {
        "servicios": servicios,
    })


