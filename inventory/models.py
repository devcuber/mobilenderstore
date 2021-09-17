from django.db import models

# Create your models here.
class Article(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    name        = models.CharField(max_length=250, verbose_name='Nombre')
    description = models.CharField(max_length=250, verbose_name='Descripción')
    code        = models.IntegerField(verbose_name='Código')
    price       = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Precio')

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return str(self.name)

class Supplier(models.Model):
    id          = models.AutoField(primary_key=True, null=False, unique=True)
    name        = models.CharField(max_length=250, verbose_name='Nombre')
    address     = models.CharField(max_length=250, verbose_name='dirección')
    articles    = models.ManyToManyField(Article)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return str(self.name)
