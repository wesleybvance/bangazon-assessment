from rest_framework import serializers
from thredsapi.models import OrderProduct

class OrderProductSerializer(serializers.ModelSerializer):
    """JSON serializer for orderProducts
    """
    class Meta:
        model = OrderProduct
        fields = ('id', 'product_id', 'order_id')
        depth = 0
