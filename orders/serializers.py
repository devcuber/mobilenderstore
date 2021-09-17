from rest_framework import serializers

from .models import Order , OrderDetail , OrderAdditionalData


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = ["id","article","quantity"]

class OrderAdditionalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAdditionalData
        fields = ["id","key","value"]

class OrderSerializer(serializers.ModelSerializer):
    details         = OrderDetailSerializer( many = True   )
    additionaldata  = OrderAdditionalDataSerializer( many = True   )
    class Meta:
        model = Order
        fields = ["id", "customer", "orderdate", "deliverydate", "isurgent", "ordertype" , "details" , "additionaldata"]
 