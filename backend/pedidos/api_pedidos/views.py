from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_pedidos.models import Restaurante, Menus, Platos, Pedido
from api_pedidos.serializers import RestauranteSerializer, MenusSerializer, PlatosSerializer, PedidoSerializer

from django.shortcuts import get_object_or_404

import decimal

# Create your views here.

####### API PROPIA #######

@api_view(['GET'])
def restaurantes_api(request):
    if request.method == 'GET':
        rtes = stub_lista_restaurantes()
        rtes_serializer = RestauranteSerializer(rtes, many=True)
        return Response(rtes_serializer.data, status=200)
    return Response({'message': 'Bad-Request, non-valid method for this endpoint'}, status=400)

@api_view(['GET'])
def platos_menus_api(request, rte_id):
    if request.method == 'GET':
        platos_y_menus = stub_platos_y_menus(rte_id)
        return Response(platos_y_menus, status=200)
    return Response({'message': 'Bad-Request, non-valid method for this endpoint'}, status=400)

@api_view(["GET", "POST"])
def pedidos_cliente_api(request, cli_id):
    if request.method == 'GET':
        pedidos = Pedido.objects.filter(cliente_ID=cli_id)
        pedido_serializer = PedidoSerializer(pedidos, many=True)
        return Response(pedido_serializer.data)

    if request.method == 'POST':
        peso = decimal.Decimal(0)
        volumen = decimal.Decimal(0)
        rte_ID = None

        for p in request.data["platos"]:
            plato = get_object_or_404(Platos, pk=p)
            peso += plato.peso
            volumen += plato.volumen

        for m in request.data["menus"]:
            menu = get_object_or_404(Menus, pk=m)
            peso += menu.peso
            volumen += menu.volumen
            rte_id = menu.restaurante_ID.restaurante_ID

        if rte_id == None:
            return Response({'message': 'Bad-Request, Can\'t ask for a delivery to a non existing entity'}, status=400)

        request.data["peso"] = peso
        request.data["volumen"] = volumen
        request.data["cliente_ID"] = cli_id
        request.data["restaurante_ID"] = rte_id

        pedido_serializer = PedidoSerializer(data = request.data)
        if not pedido_serializer.is_valid():
            return Response(pedido_serializer.errors, status=404)

        pedido_serializer.save()
        return Response(pedido_serializer.data, status=200)

    return Response({'message': 'Bad-Request, non-valid method for this endpoint'}, status=400)

####### STUBS PARA COMUNICACION CON MODULO RESTAURANTES #######

# funcion stub para consultar restaurantes
def stub_lista_restaurantes():
    return Restaurante.objects.all()

# funcion stub para consultar platos y menus
def stub_platos_y_menus(rte_id):
    menus = Menus.objects.filter(restaurante_ID=rte_id)
    platos = Platos.objects.filter(restaurante_ID=rte_id)
    platos_serializer = PlatosSerializer(platos, many=True)
    menus_serializer = MenusSerializer(platos, many=True)
    return [*platos_serializer.data, *menus_serializer.data]
