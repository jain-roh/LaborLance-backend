from rest_framework import serializers
import re
from django.contrib.auth.models import User
from LaborLance.InitialMigrations.models import CityState
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Business,JobSeeker


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username=serializers.CharField(max_length=10,min_length=10,allow_blank=False,allow_null=False)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50,min_length=8,allow_blank=False,allow_null=False)
    is_staff=serializers.BooleanField()

    class Meta:
        model = User
        fields = ['id','username','email','is_staff']
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if not re.search('^[1-9]{1}[0-9]{9}$',data['username']):
            raise serializers.ValidationError("Not a valid phone Number")
        return data


class JobSeekerSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField(max_length=200, allow_null=False)
    locations = UserSerializer(many=True)
    skills = serializers.CharField(max_length=500)
    notify = serializers.BooleanField(allow_null=False)
    minpay = serializers.FloatField(validators=[MinValueValidator(0.99)])
    maxpay = serializers.FloatField(validators=[MinValueValidator(0.99)])
    CHOICES = [('hourly', 'Hourly'),
               ('monthly', 'Monthly')]

    class Meta:
        model = JobSeeker
        fields = '__all__'



class BusinessSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField(max_length=200, allow_null=False)
    locations = serializers.PrimaryKeyRelatedField(queryset=CityState.objects.all())
    notify = serializers.BooleanField(allow_null=False)
    contactname = serializers.CharField(max_length=200, allow_null=False)
    employee_strength = serializers.IntegerField()
    industry_type = serializers.CharField(max_length=200)

    class Meta:
        model = Business
        fields = '__all__'
    def create(self, validated_data):
        return Business.objects.create(**validated_data)


