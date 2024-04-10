from rest_framework import viewsets
from .serializers import *
from rest_framework import permissions
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.views import APIView
from rest_framework import viewsets
from customer.models import *
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class OrderModelViewSet(viewsets.ModelViewSet):
    serializer_class = OrderModelSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'orders'

    def get_queryset(self):
        return OrderModel.objects.all()


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'orderitem'

    def get_queryset(self):
        return OrderItem.objects.all()


class CustomerDataViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerDataSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'customerdata'

    def get_queryset(self):
        return CustomerData.objects.all()


class DeliverDataViewSet(viewsets.ModelViewSet):
    serializer_class = DeliverDataSerializer
    permission_classes = [permissions.AllowAny]
    throttle_scope = 'deliverdata'

    def get_queryset(self):
        return DeliverData.objects.all()