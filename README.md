## DEPENDENCIAS
- Docker
- Docker-compose

## PASOS PARA SU EJECUCIÓN
Una vez con docker y docker-compose instalados,
seguir las siguientes instrucciones por línea de comandos:
`docker-compose up`

para entrar al container corriendo django:
`docker exec src_drf_app_1 -it /bin/sh`

una vez adentro del container:
`python manage.py createsuperuser # llenar los datos que pide`

ahora se puede ir a http://localhost:8000/admin/ y administrar
pedidos

luego:
http://localhost:8000/pedidos/restaurantes/ carga lista de pedidos

http://localhost:8000/pedidos/restaurantes/<id_restaurante> carga lista de menus y platos de restaurante

http://localhost:8000/pedidos/pedidos/<id_usuario> carga lista de pedidos hechos por el usuario


## PARA HACER HTTP REQUESTS DESDE JAVASCRIPT

usando `fetch` de javascript (built-in):

```
/*
llamar a esta funcion retorna los pedidos de un usuario
un pedido tiene la forma:
  {
    "pedido_ID": 1,
    "peso": "20.00",
    "volumen": "50.00",
    "precio_final": "50.00",
    "estado": null,
    "direccion": "avenida siempre viva",
    "fecha_pedido": "2021-12-04T16:56:51Z",
    "cliente_ID": 1,
    "restaurante_ID": 1,
    "menus": [
      1,
    ],
    "platos": [
      1,
    ]
  },
*/
// usuario_id es un numero llave primaria de Usuario
function get_pedidos_usuario(usuario_id)
{
  return fetch(`http://localhost:8000/pedidos/pedidos/${usuario_id}/`)
  .then((data)=>{
    return data.json();
  });
}

/*
llamar a esta funcion permite hacer un pedido si se proporcionan los datos requeridos
para hacer un pedido, pedido en el codigo de abajo es un diccionario:
  {
    direccion: "",
    precio_final: "",
    menus: [],
    platos: []
  }
platos y menus son arrays con id de platos y/o menus, por ejemplo menus = [1, 2, 3], platos = [1, 2]

*/
function post_pedido(usuario_id, pedido)
{
  fetch(`http://localhost:8000/pedidos/pedidos/${usuario_id}/`, {
    method: 'POST',
    body: JSON.stringify(pedido),
    headers: {
      'Content-Type': 'application/json',
    }
  })
  .then(res=>{
    return res.json();
  });
}

/*
llamar a esta funcion retorna lista de restaurantes
un restaurante es un objeto de la forma:
  {
  "restaurante_ID": 1,
  "direccion": "MEGA-RESTAURANTE",
  "descripcion": "Super mega restaurante bien potente"
  }
*/
function get_lista_restaurantes()
{
  return fetch(`http://localhost:8000/pedidos/restaurantes/`)
  .then((data)=>{
    return data.json();
  });
}

/*
llamar a esta funcion retorna lista de platos y menus de un restaurante
un plato es un objeto de la forma:
{
  "id": 1,
  "descripcion": "plato bien potente",
  "precio": "20.00",
  "peso": "0.50",
  "volumen": "20.00",
  "restaurante_ID": 1
}
un menu tiene la misma forma
*/
// restaurante_id es un numero llave primaria de Restaurante
function get_platos_y_menus_restaurante(restaurante_id)
{
  return fetch(`http://localhost:8000/pedidos/restaurantes/${restaurante_id}/`)
  .then((data)=>{
    return data.json();
  });
}
```
