from django.db import models
from LaborLance.InitialMigrations.models import CityState
from LaborLance.UserRegister.models import Business
from django.core.validators import MaxValueValidator, MinValueValidator

class JobPost(models.Model):
   business_id=models.ForeignKey(Business,related_name='business_user_id',null=False)
   head=models.CharField(max_length=250,null=False)
   details = models.CharField(max_length=1000,null=False)
   skills = models.CharField(max_length=200,)
   notify = models.BooleanField(null=False)

   pay=models.FloatField(validators=[MinValueValidator(0.99)],default=0.99)
   CHOICES = [('hourly', 'Hourly'),
              ('monthly', 'Monthly')]
   paytype=models.CharField(
        choices=CHOICES,
        default='hourly', max_length=2)
   is_active=models.BooleanField(default=True)
   class Meta:
      db_table = "jobpost"



