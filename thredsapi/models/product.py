from django.db import models
from .category import Category
from .threds_user import ThredsUser


class Product(models.Model):
    seller_id = models.ForeignKey(
        ThredsUser, on_delete=models.CASCADE, related_name='seller', default=1)

    name = models.CharField(max_length=200)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=7)
