from django.contrib import admin
from customers.models import CustomerType, Customer

# Register your models here.
class CustomerTypeAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'description')
    search_fields   = ('id','name')
    ordering        = ('id',)

class CustomerAdmin(admin.ModelAdmin):
    list_display    = ('id', 'name', 'code', 'photo_url', 'address', 'customertype')
    search_fields   = ('id', 'name', 'code')
    ordering        = ('id',)


admin.site.register(CustomerType, CustomerTypeAdmin)
admin.site.register(Customer    , CustomerAdmin)
