from django.contrib import admin
from inventory.models import Article, Supplier

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display    = ('id','name','description', 'code', 'price')
    search_fields   = ('id','name','code')
    ordering        = ('id',)

class SupplierAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'address')
    search_fields   = ('id', 'name')
    ordering        = ('id',)

admin.site.register(Article , ArticleAdmin)
admin.site.register(Supplier, SupplierAdmin)
