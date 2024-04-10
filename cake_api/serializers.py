from rest_framework import serializers
from customer.models import *


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class CustomerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerData
        fields = '__all__'


class DeliverDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliverData
        fields = '__all__'