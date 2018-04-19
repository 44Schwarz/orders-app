from django.shortcuts import render
from .serializers import OrderSerializer
from rest_framework import viewsets
from .models import Order

# Create your views here.


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
