from django.contrib import admin

from .models import Pedido, Restaurante, Menus, Platos, Cliente

# Register your models here.

class Admin_Pedidos(admin.ModelAdmin):
    list_display = ("pedido_ID", "precio_final", "direccion", "estado",
            "cliente_ID", "restaurante_ID", "fecha_pedido")
    list_filter = ("pedido_ID", "precio_final", "direccion", "estado",
            "cliente_ID", "restaurante_ID", "fecha_pedido")

#admin.site.register(Pedido, Admin_Pedidos)
admin.site.register(Pedido)
admin.site.register(Restaurante)
admin.site.register(Platos)
admin.site.register(Menus)
admin.site.register(Cliente)
