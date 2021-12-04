from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone

# Create your models here.
#class Admin_Pedidos(models.Model):
#    #admin_ID (PK) INT
#    #admin_pw VARCHAR
#    #admin_name VARCHAR
#    #nivel_privilegio INT
#    admin_ID = models.AutoField(primary_key=True)
#    admin_pwd = models.CharField(max_length=512)
#    admin_name = models.CharField(max_length=64)
#    nivel_privilegio = models.PositiveIntegerField()

class Cliente(models.Model):
    cliente_ID = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=512)

class Restaurante(models.Model):
    restaurante_ID = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=512)
    descripcion = models.CharField(max_length=256)

class Menus(models.Model):
    restaurante_ID = models.ForeignKey('Restaurante',on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=256)
    precio = models.DecimalField(decimal_places=2, max_digits=16)
    peso = models.DecimalField(decimal_places=2, max_digits=4)
    volumen = models.DecimalField(decimal_places=2, max_digits=4)

class Platos(models.Model):
    restaurante_ID = models.ForeignKey('Restaurante',on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=256)
    precio = models.DecimalField(decimal_places=2, max_digits=16)
    peso = models.DecimalField(decimal_places=2, max_digits=4)
    volumen = models.DecimalField(decimal_places=2, max_digits=4)

class Pedido(models.Model):
    pedido_ID = models.AutoField(primary_key=True)

    peso = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=False)
    volumen = models.DecimalField(decimal_places=2, max_digits=5, blank=False, null=False)
    precio_final = models.DecimalField(decimal_places=2, max_digits=32, blank=False, null=False)

    POSIBLES_ESTADOS = (
            (1, "Entregado"),
            (2, "En curso"),
            (3, "Cancelado"),
            )
    estado = models.PositiveSmallIntegerField(choices=POSIBLES_ESTADOS, default=1, null=True, blank=True)

    direccion = models.CharField(max_length=512, null=False, blank= False)
    fecha_pedido = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)

    cliente_ID = models.ForeignKey('Cliente', on_delete=models.SET_NULL, blank=True, null=True)
    restaurante_ID = models.ForeignKey('Restaurante', on_delete=models.SET_NULL, blank=True, null=True)

    menus = models.ManyToManyField(Menus)
    platos = models.ManyToManyField(Platos)
