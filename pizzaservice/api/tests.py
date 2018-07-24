from django.test import TestCase
from .models import Order
from rest_framework import status
from rest_framework import APIClient
from django.core.urlresolvers import reverse

# Create your tests here.
class OrderTestCase(TestCase):

    def setUp(self):
        self.pizza_id = 1
        self.pizza_size = 30
        self.customer_name = 'Jobo'
        self.customer_address = 'Weirdroad 17, 15533 Outerspace, Universe'
        self.order = Order(pizza_id=self.pizza_id, pizza_size=self.pizza_size,
        customer_name=self.customer_name, customer_address=self.customer_address)

    def test_model_can_create_an_order(self):
        old_count = Order.objects.count()
        self.order.save()
        new_count = Order.objects.count()
        self.assertNotAlmostEqual(old_count, new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.order_data = {'pizza_id': 1, 'pizza_size': 30, 'customer_name': 'Jobo', 'customer_adress': 'Weirdroad 17, 15533 Outerspace, Universe'}
        self.response = self.client.post(
            reverse('create'),
            self.order_data,
            format='json'
        )

    def test_api_can_create_an_order(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)