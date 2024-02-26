from django.urls import path
from .views import Registro, cerrar_session, Login

urlpatterns = [
    path("registro/", Registro.as_view(), name="register"),
    path("cerrar_session", cerrar_session, name="logout"),
    path("login", Login.as_view(), name="login")
]
