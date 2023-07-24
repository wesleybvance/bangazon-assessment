"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import OrderProduct, Order, Product
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
        order = request.query_params.get('order_id', None)

        if order is not None:
            order_products = order_products.filter(order_id=order)
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST requests for orderProduct"""

        order = Order.objects.get(pk=request.data['orderId'])
        product = Product.objects.get(pk=request.data['productId'])

        order_product = OrderProduct(
          order_id = order,
          product_id = product
        )

        order_product.save()
        serializer = OrderProductSerializer(order_product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
