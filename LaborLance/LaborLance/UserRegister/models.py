from django.db import models
from LaborLance.InitialMigrations.models import CityState
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class JobSeeker(models.Model):
   user_id=models.ForeignKey(User,related_name='user_id')
   name = models.CharField(max_length=200,null=False)
   locations = models.ForeignKey(CityState,related_name='locations')
   skills = models.CharField(max_length=500)
   notify = models.BooleanField(null=False)
   minpay=models.FloatField(validators=[MinValueValidator(0.99)])
   maxpay=models.FloatField(validators=[MinValueValidator(0.99)])
   CHOICES = [('hourly', 'Hourly'),
              ('monthly', 'Monthly')]
   paytype=models.CharField(
        choices=CHOICES,
        default='hourly', max_length=2)
   class Meta:
      db_table = "jobseeker"

