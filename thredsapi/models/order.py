from django.db import models
from .threds_user import ThredsUser

class Order(models.Model):
    customer_id = models.ForeignKey(
        ThredsUser, on_delete=models.CASCADE, related_name='customer', default=1)

    is_shipped = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    order_total = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    payment_type = models.CharField(null=True, max_length=100, default="")
