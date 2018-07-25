from django.shortcuts import render
from rest_framework import generics
from .serializers import OrderSerializer
from .models import Order


class OrderCreateView(generics.ListCreateAPIView):
    """This class defines the create behaviour of our rest api."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderListView(generics.ListCreateAPIView):
    """This class defines the list behaviour of our rest api."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
