from django.db import models
from django.contrib.auth.models import User



class Location(models.Model):
    name = models.CharField(max_length=200)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    
# class UserInfo(models.Model):
#     user = models.ForeignKey(User,related_name='user-userinfo')
#     location = models.ForeignKey(Location,related_name='userinfo-location')
#     adress = models.CharField(max_length=200)
#     city = models.CharField(max_length=200)