# Mobilenderstore

Mobilender en una plataforma demo, para el control de pedidos para una empresa de productos electronicos

## Uso

El demo puede usarse en el siguiente enlace:
[mobilenderstore.herokuapp.com](https://mobilenderstore.herokuapp.com/)

La parte administrativa se puede usar acceder desde el siguiente enlace:
[Admin](https://mobilenderstore.herokuapp.com/admin)

El api-rest se puede consumir desde el siguiente enlace:
[ApiRest](https://mobilenderstore.herokuapp.com/rest)

## Diseño Base de datos

![alt text](https://photos.google.com/share/AF1QipMNNgNKHdcT2cZmBqTbHFss9jMDG0W-7olgFNa3DYBfAiL6-ayGhFtt-EezjMUsxg/photo/AF1QipO84Y2d8M7I2VGddAUqpYm5zmfg6elTlMCsYlkJ?key=RWl2QWVRUERESlE1aUJPLXB3bXF6M09FR0RnV0NR)

La tabla de OrderAdditionalData es útil para almacenar datos extra de las órdenes y que esta información puede ser diferente según el tipo de orden:

Si el pedido es hacia el Centro de distribución:
1. Almacén

Si el pedido es hacia una sucursal:
1. Referencia (Alfanumérico).
2. Código de sucursal que surtirá el pedido (Numérico).

Si el pedido es hacia una empresa asociada:
1. Referencia (Alfanumérico).
2. Código de Socio (Numérico).
3. Detalle del pedido (una o más entradas):
