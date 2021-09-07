from django.db import models
from customers.models import Customer
from inventory.models import Article

# Create your models here.
class OrderType(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    name        = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de Orden'
        verbose_name_plural = 'Tipos de orden'

class Order(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    customer    = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    orderdate   = models.DateTimeField(verbose_name='Fecha de orden')
    deliverydate= models.DateTimeField(verbose_name='Fecha de entrega')
    isurgent    = models.BooleanField (verbose_name='Es urgente?' , default = False )
    ordertype   = models.ForeignKey(OrderType, on_delete=models.CASCADE, verbose_name='Cliente')

    class Meta:
        verbose_name = 'Orden'
        verbose_name_plural = 'Ordenes'

class OrderDetail(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    order       = models.ForeignKey(Order,   on_delete=models.CASCADE, verbose_name='Orden')
    article     = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Articulo')
    quantity    = models.IntegerField(verbose_name='Cantidad')

    class Meta:
        verbose_name = 'Detalle de orden'
        verbose_name_plural = 'Detalles de ordenes'

class OrderAdditionalData(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    order       = models.ForeignKey(Order,   on_delete=models.CASCADE, verbose_name='Orden')
    key         = models.CharField(max_length=250, verbose_name='llave del campo adicional')
    value       = models.CharField(max_length=250, verbose_name='valor del campo adicional')

    class Meta:
        verbose_name = 'Informacion adicional de orden'
        verbose_name_plural = 'Informacion adicional de ordenes'
