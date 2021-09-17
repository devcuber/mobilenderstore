from django.contrib import admin
from orders.models import OrderType, Order, OrderDetail , OrderAdditionalData

# Register your models here.
class OrderTypeAdmin(admin.ModelAdmin):
    list_display  = ('id', 'name', 'description')
    search_fields = ('id', 'name')
    ordering      = ('id',)

class OrderDetailInline(admin.TabularInline):
    model = OrderDetail

class OrderAdditionalDataInline(admin.TabularInline):
    model = OrderAdditionalData

class OrderAdmin(admin.ModelAdmin):
    list_display  = ('id', 'customer', 'orderdate', 'deliverydate', 'isurgent', 'ordertype' )
    search_fields = ('id', 'customer', 'isurgent' , 'ordertype')
    ordering      = ('id',)
    inlines = [ OrderDetailInline, OrderAdditionalDataInline]

admin.site.register(OrderType , OrderTypeAdmin)
admin.site.register(Order     , OrderAdmin)
