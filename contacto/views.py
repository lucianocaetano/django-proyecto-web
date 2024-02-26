from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.views import View
from smtplib import SMTPAuthenticationError
from django.core.mail import send_mail
#contact views

class index(View):

    def get(self, request, *args, **kwargs):

        form=FormularioContacto()

        return render(request, "contacto/index.html", {
            "form": form
        })

    def post(self, request, *args, **kwargs):
        form=FormularioContacto(data=request.POST)

        if form.is_valid():

            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            try:
                send_mail(
                    'Message desde App de Django',
                    'El usuario {} con la direccion {} escribe lo siguiente: \n {}'.format(nombre, email, contenido),
                    email,
                    ['lucianocaetano1999@gmail.com'],
                    fail_silently=False,
                )

                print("hola")
            except SMTPAuthenticationError as e:
                print(e)
                return redirect("/contacto?validate='{}'".format(e))


            return redirect("contacto")


        return redirect("contacto")



