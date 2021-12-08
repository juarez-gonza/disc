docker:

`docker-compose up
docker exec src_drf_app_1 -it /bin/sh`

una vez adentro del container:
`python manage.py createsuperuser # llenar los datos que pide`

ahora se puede ir a http://localhost:8000/admin/ y administrar
pedidos

luego:
http://localhost:8000/pedidos/restaurantes/ carga lista de pedidos

http://localhost:8000/pedidos/restaurantes/<id_restaurante> carga lista de menus y platos de restaurante

http://localhost:8000/pedidos/pedidos/<id_usuario> carga lista de pedidos hechos por el usuario
