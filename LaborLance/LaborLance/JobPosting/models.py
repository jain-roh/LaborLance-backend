from django.db import models
from LaborLance.InitialMigrations.models import CityState,Skill
from LaborLance.UserRegister.models import Business,JobSeeker
from django.core.validators import MaxValueValidator, MinValueValidator

class JobPost(models.Model):
   business_id=models.ForeignKey(Business,related_name='business_user_id',null=False)
   head=models.CharField(max_length=250,null=False)
   details = models.CharField(max_length=1000,null=False)
   skills = models.ManyToManyField(Skill)
   notify = models.BooleanField(null=False)
   awarded_to=models.ForeignKey(JobSeeker,related_name='awarded_jobseeker_id',null=True,default=None)
   pay=models.FloatField(validators=[MinValueValidator(0.99)],default=0.99)
   # datafile = models.FileField(blank=False, null=False)
   CHOICES = [('hourly', 'Hourly'),
              ('monthly', 'Monthly')]
   paytype=models.CharField(
        choices=CHOICES,
        default='hourly', max_length=2)
   is_active=models.BooleanField(default=True)
   class Meta:
      db_table = "jobpost"

   def __str__(self):
      return self.head



class JobPostImages(models.Model):
   post_id=models.ForeignKey(JobPost,related_name='post_id',null=False)
   files = models.FileField(blank=False, null=False)
   is_active=models.BooleanField(default=True)
   class Meta:
      db_table = "postimage"


class JobBid(models.Model):
   jobseeker_id=models.ForeignKey(JobSeeker,related_name='jobseekeruser_id',null=False)
   post_id=models.ForeignKey(JobPost,related_name='job_post_id',null=False)
   head=models.CharField(max_length=250,null=False)
   details = models.CharField(max_length=1000,null=False)
   pay=models.FloatField(validators=[MinValueValidator(0.99)],default=0.99)
   # datafile = models.FileField(blank=False, null=False)
   CHOICES = [('hourly', 'Hourly'),
              ('monthly', 'Monthly')]
   paytype=models.CharField(
        choices=CHOICES,
        default='hourly', max_length=2)
   is_active=models.BooleanField(default=True)
   class Meta:
      db_table = "jobbid"

   def __str__(self):
      return self.head
