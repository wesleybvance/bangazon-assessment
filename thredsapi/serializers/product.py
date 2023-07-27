from rest_framework import serializers
from thredsapi.models import Product

class DecimalToNumber(serializers.DecimalField):
    def to_representation(self, value):
        value = super().to_representation(value)
        return float(value)
class ProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products
    """
    price = DecimalToNumber(max_digits=7, decimal_places=2)
    class Meta:
        model = Product
        fields = ('id', 'seller_id', 'name', 'photo_url',
                  'category_id', 'description', 'price', 'is_available')
