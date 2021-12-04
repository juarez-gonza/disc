from django.urls import path

from . import views

urlpatterns = [
    path('restaurantes/', views.restaurantes_api, name='restaurantes'),
    path('restaurantes/<int:rte_id>/', views.platos_menus_api, name='platos y menus'),
    path('pedidos/<int:cli_id>/', views.pedidos_cliente_api, name='pedidos del cliente')
]
