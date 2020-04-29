from rest_framework import serializers
import re
from django.contrib.auth.models import User
from LaborLance.InitialMigrations.models import CityState
from django.core.validators import MaxValueValidator, MinValueValidator
from LaborLance.UserRegister.models import Business
from .models import JobPost
from LaborLance.master.serializer import CityStateSerializer




class JobPostSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    business_id=serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())
    head = serializers.CharField(max_length=250, allow_null=False)
    details = serializers.CharField(max_length=1000, allow_null=False)
    skills = serializers.CharField(max_length=200, )
    notify = serializers.BooleanField(allow_null=False)

    pay = serializers.FloatField(validators=[MinValueValidator(0.99)], default=0.99)
    CHOICES = [('hourly', 'Hourly'),
               ('monthly', 'Monthly')]
    paytype = serializers.ChoiceField(
        choices=CHOICES,
        default='hourly')
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = JobPost
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return JobPost.objects.create(**validated_data)



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
#
# class BusinessSerializer(UserSerializer):
#     id = serializers.ReadOnlyField()
#     # user_id=serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     name = serializers.CharField(max_length=200, allow_null=False)
#     locations = serializers.PrimaryKeyRelatedField(queryset=CityState.objects.all())
#     notify = serializers.BooleanField(allow_null=False)
#     contactname = serializers.CharField(max_length=200, allow_null=False)
#     employee_strength = serializers.IntegerField()
#     industry_type = serializers.CharField(max_length=200)
#
#     class Meta:
#         model = Business
#         fields = '__all__'
#     def create(self, validated_data):
#         return Business.objects.create(**validated_data)
#

