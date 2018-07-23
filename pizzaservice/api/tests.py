from django.test import TestCase
from .models import Order

# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        self.pizza_id = 1
        self.pizza_size = "30cm"
        self.customer_name = "Jobo"
        self.customer_address = "Weirdroad 17, 15533 Outerspace, Universe"
        self.order = Order(pizza_id=self.pizza_id, pizza_size=self.pizza_size,
        customer_name=self.customer_name, customer_address=self.customer_address)

    def test_model_can_create_an_order(self):
        old_count = Order.objects.count()
        self.order.save()
        new_count = Order.objects.count()
        self.assertNotAlmostEqual(old_count, new_count)