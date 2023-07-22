from rest_framework import serializers
from thredsapi.models import ThredsUser

class ThredsUserSerializer(serializers.ModelSerializer):
    """JSON serializer for threds user
    """
    class Meta:
        model = ThredsUser
        fields = ('id', 'first_name', 'last_name', 'username', 'image_url', 'uid', 'address')
