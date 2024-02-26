from django.db import models

class Servicios(models.Model):

    class Meta:
        verbose_name="Servicio"
        verbose_name_plural="Servicios"

    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to="servicios")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo


