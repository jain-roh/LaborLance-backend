from rest_framework import serializers
import re
from django.contrib.auth.models import User
from LaborLance.InitialMigrations.models import CityState
from django.core.validators import MaxValueValidator, MinValueValidator
from LaborLance.InitialMigrations.models import CityState


class CityStateSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    city = serializers.CharField(max_length=200)
    state = serializers.CharField(max_length=200)
    population = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=100)
    pop_class = serializers.CharField(max_length=100)
    class Meta:
        model = CityState
        fields = '__all__'



