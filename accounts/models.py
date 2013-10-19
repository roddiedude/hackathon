from django.db import models
from django.contrib.auth.models import User
from location.models import Location

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User,related_name='user-userinfo')
    location = models.ForeignKey(Location,related_name='userinfo-location')
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    