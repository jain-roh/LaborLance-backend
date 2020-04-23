from rest_framework import serializers
import re
from django.contrib.auth.models import User
class UserSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=10,min_length=10,allow_blank=False,allow_null=False)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50,min_length=8,allow_blank=False,allow_null=False)
    is_staff=serializers.BooleanField()

    class Meta:
        model = User
        fields = ('username', 'password', 'email','is_staff')

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if not re.search('^[1-9]{1}[0-9]{9}$',data['username']):
            raise serializers.ValidationError("Not a valid phone Number")
        return data

