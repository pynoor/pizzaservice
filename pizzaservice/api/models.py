from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_pizza_size(value):
    if value not in (30, 50):
        raise ValidationError(
            _("That's a strange pizza. Try a different size.")
        )

# Create your models here.
class Order(models.Model):
    id = models.AutoField(primary_key=True)
    pizza_id = models.IntegerField()
    pizza_size = models.IntegerField(validators=[validate_pizza_size])
    customer_name = models.CharField(max_length=50)
    customer_address = models.CharField(max_length=250)

    def __str__(self):
        return str(self.pizza_id)
