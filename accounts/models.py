from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserInfo(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=2000)
    location = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    