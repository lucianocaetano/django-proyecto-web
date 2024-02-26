from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.html import strip_tags
from django.core.mail import send_mail
from .models import Pedido, LineaPedido
from django.shortcuts import render
from django.contrib import messages
from carrito.Carro import Carro
from django.template.loader import render_to_string

def enviar_email(pedido=None, lineas_pedido=None, username=None, email=None):
    asunto="Gracias por el mensaje"
    message=render_to_string("email/pedido.html", {
        "pedido": pedido,
        "lineas_pedido": lineas_pedido,
        "username": username,
        "email": email
    })

    message_text=strip_tags(message)
    from_email="email@email.com"
    to=email
    send_mail(asunto, message_text, from_email, [to], html_message=message)

    pass
@login_required(login_url="/auth/login")
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)

    carro=Carro(request)

    lineas_pedido=list()

    for key, value in carro.carro.items():

        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido
        ))

    LineaPedido.objects.bulk_create(lineas_pedido)
    enviar_email(pedido=pedido, lineas_pedido=lineas_pedido, username=request.user.username, email=request.user.email)
    messages.success(request, "El Pedido se ha creado exitosamente")

    return redirect("tienda")


