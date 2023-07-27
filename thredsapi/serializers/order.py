from rest_framework import serializers
from thredsapi.models import Order

class DecimalToNumber(serializers.DecimalField):
    def to_representation(self, value):
        value = super().to_representation(value)
        return float(value)
class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders
    """
    order_total = DecimalToNumber(max_digits=10, decimal_places=2)
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'is_shipped', 'is_open', 'order_total', 'payment_type')
