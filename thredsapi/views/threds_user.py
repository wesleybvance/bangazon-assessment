"""View module for handling requests about orderProducts"""
# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q
from thredsapi.models import ThredsUser, Order
from thredsapi.serializers import ThredsUserSerializer
from thredsapi.serializers import OrderSerializer



class ThredsUserView(ViewSet):
    """Threds user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Threds user

        Returns:
            Response -- JSON serialized Threds user
        """
        threds_user = ThredsUser.objects.get(pk=pk)
        serializer = ThredsUserSerializer(threds_user)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all Threds users

        Returns:
            Response -- JSON serialized list of Threds users
        """
        threds_users = ThredsUser.objects.all()
        serializer = ThredsUserSerializer(threds_users, many=True)
        return Response(serializer.data)

    def create(self, request):
        """POST request to create a Threds user"""
        uid = request.META["HTTP_AUTHORIZATION"]
        serializer = ThredsUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(uid=uid)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """PUT request to update a Threds user"""
        threds_user = ThredsUser.objects.get(pk=pk)
        uid = request.META["HTTP_AUTHORIZATION"]
        threds_user.first_name = request.data['firstName']
        threds_user.last_name = request.data['lastName']
        threds_user.username = request.data['username']
        threds_user.image_url = request.data['imageUrl']
        threds_user.address = request.data['address']
        threds_user.uid = uid
        threds_user.save()
        return Response({'message': 'Threds User Updated'}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """DELETE request to delete a Threds user"""
        threds_user=ThredsUser.objects.get(pk=pk)
        threds_user.delete()
        return Response({'message': 'User Deleted'}, status=status.HTTP_204_NO_CONTENT)

    @action(methods=['post'], detail=True, url_path='check_cart', url_name='check_cart')
    def check_cart(self, request, pk):
        """POST request to check if an open order
        exists for the current user"""

        open_cart = Order.objects.filter(
            Q(customer_id=pk) & Q(is_open=True))

        serializer = OrderSerializer(open_cart, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(open_cart, status=status.HTTP_200_OK)
