from rest_framework import serializers
from thredsapi.models import Order

class OrderSerializer(serializers.ModelSerializer):
    """JSON serializer for orders
    """
    class Meta:
        model = Order
        fields = ('id', 'customer_id', 'is_shipped', 'is_open', 'order_total', 'payment_type')
