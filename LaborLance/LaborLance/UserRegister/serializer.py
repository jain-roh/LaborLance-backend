from rest_framework import serializers
import re
from django.contrib.auth.models import User
from LaborLance.InitialMigrations.models import CityState,Skill
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Business,JobSeeker
from LaborLance.master.serializer import CityStateSerializer

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


class JobSeekerSerializer(UserSerializer):
    id=serializers.ReadOnlyField()
    # user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField(max_length=200, allow_null=False)
    locations = serializers.PrimaryKeyRelatedField(many=True, allow_null=False,allow_empty=False,read_only=False, queryset=CityState.objects.all(), source='location')
    skills = serializers.PrimaryKeyRelatedField(many=True, allow_null=False,allow_empty=False,read_only=False, queryset=Skill.objects.all(), source='skill')
    notify = serializers.BooleanField(allow_null=False)
    minpay = serializers.FloatField(validators=[MinValueValidator(0.99)])
    maxpay = serializers.FloatField(validators=[MinValueValidator(0.99)])
    CHOICES = [('hourly', 'Hourly'),
               ('monthly', 'Monthly')]
    paytype = serializers.ChoiceField(
        choices=CHOICES,
        default='hourly')
    is_staff = serializers.BooleanField(read_only=True,default=True)

    class Meta:
        model = JobSeeker
        fields = '__all__'
        read_only_fields = ('is_active', 'is_staff')

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        location = validated_data.pop('location')
        pwd=validated_data.pop('password')
        validated_data['is_staff']=True
        skills=validated_data.data.pop('skill')
        js = JobSeeker.objects.create(**validated_data)
        try:
            js.set_password(pwd)
            js.save()
            for obj in list(location):
                js.location.add(obj)
                js.save()
            for obj in list(skills):
                js.skills.add(obj)
                js.save()

        except Exception as e:
            js.delete()

        return js



    # def save(self):
    # #     # if not commit:
    # #     #     raise NotImplementedError("Can't create User and Userextended without database save")
    # #     # user = super().save(*args, **kwargs)
    # #     print(self.data)
    # #     user=User.objects.get(pk=self.data['user_id'])
    # #     js = JobSeeker.objects.create(user_id=user,name=self.data['name'],notify=self.data['notify'],skills=self.data['skills'],)
    #
    #     # js=JobSeekerSerializer(js)
    #     try:
    #         for obj in list((self.data['locations'])):
    #             print(obj)
    #             js.location.add(CityState.objects.get(pk=obj))
    #     except Exception as e:
    #         print('Error',e)
    #     return JobSeekerSerializer()
# {
# "user_id":1,
# "name":"Rohit Jain",
# "locations":[{"id":1},{"id":2}],
# "skills":"None",
# "notify":true,
# "minpay":25,
# "maxpay":26
# }

class BusinessSerializer(UserSerializer):
    id = serializers.ReadOnlyField()
    # user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    name = serializers.CharField(max_length=200, allow_null=False)
    locations = serializers.PrimaryKeyRelatedField(queryset=CityState.objects.all())
    notify = serializers.BooleanField(allow_null=False)
    contactname = serializers.CharField(max_length=200, allow_null=False)
    employee_strength = serializers.IntegerField()
    industry_type = serializers.CharField(max_length=200)
    is_staff = serializers.BooleanField(read_only=True,default=True)

    class Meta:
        model = Business
        fields = '__all__'
        read_only_fields = ('is_active', 'is_staff')
    def create(self, validated_data):
        pwd = validated_data.pop('password')
        validated_data['is_staff'] = False
        bs=Business.objects.create(**validated_data)
        try:
            bs.set_password(pwd)
            bs.save()
        except Exception as e:
            bs.delete()
        return bs


