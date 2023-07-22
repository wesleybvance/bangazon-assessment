"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import ThredsUser


class ThredsUserView(ViewSet):
    """Threds user view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single Threds user

        Returns:
            Response -- JSON serialized Threds user
        """


    def list(self, request):
        """Handle GET requests to get all Threds users

        Returns:
            Response -- JSON serialized list of Threds users
        """
