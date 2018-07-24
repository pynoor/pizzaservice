from rest_framework import serializers
from .models import Order

#TODO: fix this, create virtual environment
class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = ('pizza_id', 'pizza_size', 'customer_name', 'customer_address')

