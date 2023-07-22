"""View module for handling requests about orderProducts"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from thredsapi.models import OrderProduct


class OrderProductView(ViewSet):
    """Threds orderProduct view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single orderProduct

        Returns:
            Response -- JSON serialized orderProduct
        """


    def list(self, request):
        """Handle GET requests to get all orderProducts

        Returns:
            Response -- JSON serialized list of orderProducts
        """
