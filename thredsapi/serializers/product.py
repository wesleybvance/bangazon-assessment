from rest_framework import serializers
from thredsapi.models import Product


class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products
    """
    class Meta:
        model = Product
        fields = ('id', 'seller_id', 'name', 'photo_url',
                  'category_id', 'description', 'price', 'is_available')
