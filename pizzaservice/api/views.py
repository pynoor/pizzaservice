from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order

# Create your views here.

class OrderCreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest api."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()
