from api_pedidos.models import Restaurante, Menus, Platos
from rest_framework import serializers

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurante
        fields = '__all__'

class PlatosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platos
        fields = '__all__'

class MenusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menus
        fields = '__all__'
