from rest_framework.response import Response
from rest_framework.decorators import api_view
from api_pedidos.models import Restaurante, Menus, Platos
from api_pedidos.serializers import RestauranteSerializer, MenusSerializer, PlatosSerializer

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
