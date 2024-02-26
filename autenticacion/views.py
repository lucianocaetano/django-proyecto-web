from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

class Registro(View):

    def get(self, request):
        form = UserCreationForm()

        return render(request, "auth/register.html", {
            "form": form
        })

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():

            usuario = form.save()
            login(request, usuario)

            return redirect("index")

        for msg in form.error_messages:
            messages.error(request, form.error_messages[msg])

        return render(request, "auth/register.html", {
            "form": form
        })

def cerrar_session(request):

    logout(request)

    return redirect("index")

class Login(View):

    def get(self, request):
        form = AuthenticationForm()

        return render(request, "auth/login.html", {
            "form": form
        })

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")

            user=authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")

            else:
                messages.error(request, "usuario no valido")
        else:
            messages.error(request, "datos incorrectos")

        return render(request, "auth/login.html", {
            "form": form
        })

