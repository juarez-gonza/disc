from django.contrib import admin

from .models import Pedido

# Register your models here.

class Admin_Pedidos(admin.ModelAdmin):
    list_display = ("pedido_ID", "precio_final", "direccion", "estado",
            "cliente_ID", "restaurante_ID", "fecha_pedido")
    list_filter = ("pedido_ID", "precio_final", "direccion", "estado",
            "cliente_ID", "restaurante_ID", "fecha_pedido")

admin.site.register(Pedido, Admin_Pedidos)
