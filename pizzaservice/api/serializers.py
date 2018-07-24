from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:

        model = Order
        fields = ('id', 'pizza_id', 'pizza_size', 'customer_name', 'customer_address')

    #Attention! Can't just add 'id' fiel here ..
    #Error : django.core.exceptions.ImproperlyConfigured: Field name `id` is not valid for model `Order`.
    #This is because I have manually set a primary key so the automatic id is not added. Gotta fix that.