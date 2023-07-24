"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import ThredsUser
from thredsapi.serializers import ThredsUserSerializer


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
