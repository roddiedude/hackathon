from django.db import models
from django.contrib.auth.models import User
from category.models import Category

# Create your models here.
class Complaint(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=2000)
    user = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    locality = models.CharField(max_length=200)
    address = models.CharField(max_length=2000)
    date_entered = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True)
    upvotes = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="complaints", null=True)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    
class Comments(models.Model):
    complaint = models.ForeignKey(Complaint)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)
    

    