"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import Order, ThredsUser, OrderProduct, Product
from thredsapi.serializers import OrderSerializer


class OrderView(ViewSet):
    """Threds order view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single order

        Returns:
            Response -- JSON serialized order
        """
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all orders

        Returns:
            Response -- JSON serialized list of orders 
        """
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request for order"""
        customer_id=ThredsUser.objects.get(pk=request.data['customerId'])

        order = Order(
          customer_id=customer_id,
        )

        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request for updating an order"""

        order = Order.objects.filter(pk=pk).first()

        customer = ThredsUser.objects.get(pk=request.data['customerId'])
        order.customer_id = customer
        order.order_total = request.data["orderTotal"]
        order.save()

        return Response({'message': 'Order updated'}, status=status.HTTP_204_NO_CONTENT)
