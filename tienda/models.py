from django.db import models

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name="Categoria"
        verbose_name_plural="Categorias de Productos"

class Producto(models.Model):

    nombre = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponabilidad = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    class Meta():

        verbose_name="Producto"
        verbose_name_plural="Productos"
