from django.db import models
from .product import Product
from .order import Order


class OrderProduct(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product', default=1)

    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    total = models.DecimalField(max_digits=10)
