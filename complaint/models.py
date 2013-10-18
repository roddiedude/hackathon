from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Complaint(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    location = models.CharField(max_length=200)
    date_entered = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True)
    upvotes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="complaints", null=True)
    