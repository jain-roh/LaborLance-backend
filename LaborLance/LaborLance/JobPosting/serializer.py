from rest_framework import serializers
import re
from django.contrib.auth.models import User
from LaborLance.InitialMigrations.models import CityState
from django.core.validators import MaxValueValidator, MinValueValidator
from LaborLance.UserRegister.models import Business,JobSeeker
from .models import JobPost,JobPostImages,JobBid
from LaborLance.master.serializer import CityStateSerializer




class JobPostSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    business_id=serializers.PrimaryKeyRelatedField(queryset=Business.objects.all())
    head = serializers.CharField(max_length=250, allow_null=False)
    details = serializers.CharField(max_length=1000, allow_null=False)
    skills = serializers.CharField(max_length=200, )
    notify = serializers.BooleanField(allow_null=False)
    awarded_to = serializers.PrimaryKeyRelatedField(required=False,read_only=True)

    pay = serializers.FloatField(validators=[MinValueValidator(0.99)], default=0.99)
    CHOICES = [('hourly', 'Hourly'),
               ('monthly', 'Monthly')]
    paytype = serializers.ChoiceField(
        choices=CHOICES,
        default='hourly')
    is_active = serializers.BooleanField(default=True)
    # datafile=serializers.FileField()
    class Meta:
        model = JobPost
        fields = '__all__'


    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return JobPost.objects.create(**validated_data)

class JobPostImageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    post_id = serializers.PrimaryKeyRelatedField(queryset=JobPost.objects.all())
    files=serializers.FileField()
    is_active = serializers.BooleanField(default=True)

    # datafile=serializers.FileField()
    class Meta:
        model = JobPostImages
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return JobPostImages.objects.create(**validated_data)

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
class JobBidSerializer(serializers.Serializer):
    id=serializers.ReadOnlyField()
    jobseeker_id = serializers.PrimaryKeyRelatedField(queryset=JobSeeker.objects.all())
    post_id = serializers.PrimaryKeyRelatedField(queryset=JobPost.objects.all())
    head = serializers.CharField(max_length=250, allow_null=False)
    details = serializers.CharField(max_length=1000, allow_null=False)
    pay = serializers.FloatField(validators=[MinValueValidator(0.99)], default=0.99)
    # datafile = models.FileField(blank=False, null=False)
    CHOICES = [('hourly', 'Hourly'),
               ('monthly', 'Monthly')]
    paytype = serializers.ChoiceField(
        choices=CHOICES,
        default='hourly')
    is_active = serializers.BooleanField(default=True)
    # datafile=serializers.FileField()
    class Meta:
        model = JobBid
        fields = '__all__'

    def create(self, validated_data):
        # user = User.objects.get(pk=self.data['user_id'])
        return JobBid.objects.create(**validated_data)
