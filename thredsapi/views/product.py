"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import Product, ThredsUser
from thredsapi.serializers import ProductSerializer


class ProductView(ViewSet):
    """Threds product view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single product

        Returns:
            Response -- JSON serialized product
        """
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all products

        Returns:
            Response -- JSON serialized list of products
        """
        products = Product.objects.all().order_by('-id')
        seller = request.query_params.get('seller_id', None)
        category = request.query_params.get('category_id', None)
        if seller is not None:
            products = products.filter(seller_id = seller)
        if category is not None:
            products = products.filter(category_id = category)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request for product"""
        seller_id = ThredsUser.objects.get(pk=request.data["sellerId"])

        product = Product(
          name=request.data['name'],
          photo_url=request.data['photoUrl'],
          category_id=request.data['categoryId'],
          description=request.data['description'],
          price=request.data['price'],
          seller_id=seller_id,
        )

        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
