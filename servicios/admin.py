from django.contrib import admin
from .models import Servicios

class ServicioAdmin(admin.ModelAdmin):

    readonly= ("created", "updated")

admin.site.register(Servicios, ServicioAdmin)
