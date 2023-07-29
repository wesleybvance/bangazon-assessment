"""View module for handling requests about orderProducts"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from thredsapi.models import Order, ThredsUser, OrderProduct
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
        customer_id = ThredsUser.objects.get(pk=request.data['customerId'])

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
        order.is_open = request.data["isOpen"]
        order.save()

        return Response({'message': 'Order updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to delete an order"""
        order = Order.objects.get(pk=pk)
        order.delete()
        return Response({'message': 'Order Deleted'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True, url_path='calculate_total', url_name='calculate_total')
    def calculate_total(self, request, pk):
        """POST request to calculate the total of 
        an order from the orderProducts"""

        all_order_products = OrderProduct.objects.all()
        order_products = all_order_products.filter(order_id=pk)

        total = 0
        for o_p in order_products:
            total += o_p.product_id.price
        return Response(total, status=status.HTTP_200_OK)

    # @action(methods=['post'], detail=True, url_path='check_product', url_name='check_product')
    # def check_product(self, request, pk):
    #     """POST request to evaluate whether
    #     a product's id matches any product_ids in
    #     a list of order_products"""
    #     order_products = OrderProduct.objects.filter(order_id=pk)
    #     new_product_id = request.data['productId']

    #     checked_ids = [product.product_id for product in order_products]

    #     if new_product_id in checked_ids:
    #         return Response(True)
    #     else:
    #         return Response(False)

    @action(methods=['post'], detail=True, url_path='check_product', url_name='check_product')
    def check_product(self, request, pk):
        """POST request to evaluate whether
        a product's id matches any product_ids in
        a list of order_products"""
        order_products = OrderProduct.objects.filter(order_id=pk)

        for product in order_products:
            if product.product_id == request.data['productId']:
                return Response(True)

        return Response(False)
