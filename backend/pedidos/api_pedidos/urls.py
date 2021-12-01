from django.urls import path

from . import views

urlpatterns = [
    path('restaurantes/', views.restaurantes_api, name='restaurantes'),
    path('restaurantes/<int:rte_id>/', views.platos_menus_api, name='platos y menus')
]
