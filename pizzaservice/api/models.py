from django.db import models

# Create your models here.
class Order(models.Model):

    pizza_id = models.IntegerField(primary_key=1)
    pizza_size = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.pizza_id)