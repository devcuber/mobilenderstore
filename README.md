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

![base de datos](https://lh3.googleusercontent.com/pw/AM-JKLVXTcQsoZfXN5oHxDhUlmUKKhUPpbU_-QTacVVrB5vpuf2fnX918VgLvzwbR-B2lRJl0ST-r7o6PWmJni-MKGca2XCdcJTDFYcI2U8v_sgPOgeCCjEzuBCh_MR0WXt3XvM6X94H9QDDFimHRA8V1ve9nA=w960-h697-no?authuser=0.jpg)

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
