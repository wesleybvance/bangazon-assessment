"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import OrderProduct
from thredsapi.serializers import OrderProductSerializer

class OrderProductView(ViewSet):
    """Threds orderProduct view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single orderProduct

        Returns:
            Response -- JSON serialized orderProduct
        """
        order_product = OrderProduct.objects.get(pk=pk)
        serializer = OrderProductSerializer(order_product)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all orderProducts

        Returns:
            Response -- JSON serialized list of orderProducts
        """
        order_products = OrderProduct.objects.all()
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data)
