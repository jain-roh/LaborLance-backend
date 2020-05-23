from django.db import models

class CityState(models.Model):
   city = models.CharField(max_length=200)
   state = models.CharField(max_length=200)
   population = models.CharField(max_length=200)
   type = models.CharField(max_length=100)
   pop_class=models.CharField(max_length=100)
   class Meta:
      db_table = "citystate"

   def __str__(self):
      return self.city


class Skill(models.Model):
   skill = models.CharField(max_length=200)
   class Meta:
      db_table = "skill"

   def __str__(self):
      return self.skill