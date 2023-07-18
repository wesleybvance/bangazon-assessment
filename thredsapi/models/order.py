from django.db import models
from .threds_user import ThredsUser
from .order_product import OrderProduct


class Order(models.Model):
    customer_id = models.ForeignKey(
        ThredsUser, on_delete=models.CASCADE, related_name='customer', default=1)

    is_shipped = models.BooleanField(default=True)
    is_open = models.BooleanField(default=True)
    order_product_id = models.ForeignKey(
        OrderProduct, on_delete=models.CASCADE, related_name='orderProduct')
    order_total = models.DecimalField(max_digits=10)
    payment_type = models.CharField(max_length=100)
