from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ProyectoWebApp.urls")),
    path("servicios/", include("servicios.urls")),
    path("blog/", include("blog.urls")),
    path("contacto/", include("contacto.urls")),
    path("tienda/", include("tienda.urls")),
    path("carro/", include(("carrito.urls", "carrito"), namespace="carro")),
    path("auth/", include("autenticacion.urls")),
    path("pedido/", include("pedidos.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

