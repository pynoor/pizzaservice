from django.test import TestCase
from .models import Order
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse

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
        self.order_data = {'pizza_id': 1, 'pizza_size': 30, 'customer_name': 'Jobo', 'customer_address': 'Weirdroad 17, 15533 Outerspace, Universe'}
        self.response = self.client.post(
            reverse('create'),
            self.order_data,
            format='json'
            )

    def test_api_can_create_an_order(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_an_order(self):
        order = Order.objects.get()
        response = self.client.get(
            reverse('details', kwargs={'pk': order.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, order)

    def test_api_can_delete_an_order(self):
        order = Order.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': order.id}),
            format='json',
            follow=True
        )
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_api_can_update_an_order(self):
        order = Order.objects.get()
        change_order = {'pizza_id': 2, 'pizza_size': 30, 'customer_name': 'Jobo', 'customer_address': 'Weirdroad 17, 15533 Outerspace, Universe'}
        response = self.client.put(
            reverse('details', kwargs={'pk': order.id}),
            change_order,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

