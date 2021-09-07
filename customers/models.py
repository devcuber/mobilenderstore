from django.db import models

# Create your models here.
class CustomerType(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    name        = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')

    class Meta:
        verbose_name = 'Tipo de cliente'
        verbose_name_plural = 'Tipos de clientes'

class Customer(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    name        = models.CharField(max_length=250, verbose_name='Nombre')
    code        = models.CharField(max_length=250, verbose_name='Código')
    photo_url   = models.CharField(max_length=250, verbose_name='foto')
    address     = models.CharField(max_length=250, verbose_name='dirección')
    customertype= models.ForeignKey(CustomerType, on_delete=models.CASCADE, verbose_name='Tipo de cliente')

    class Meta:
        verbose_name = 'Tipo de cliente'
        verbose_name_plural = 'Tipos de cliente'
