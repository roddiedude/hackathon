from django.db import models

# Create your models here.
class Ward(models.Model):
    name = models.CharField(max_length=200)