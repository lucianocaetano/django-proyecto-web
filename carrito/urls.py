from .views import agregar_carro, eliminar_carro, limpiar_carro, restar_producto
from django.urls import path

urlpatterns = [
    path("agregar/<int:pk>", agregar_carro, name="agregar"),
    path("eliminar/<int:pk>", eliminar_carro),
    path("restar/<int:pk>", restar_producto, name="restar"),
    path("limpiar", limpiar_carro)
]
