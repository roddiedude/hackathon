from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from location.models import Location
from django.utils import timezone

# Create your models here.
class Complaint(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=2000)
    user = models.ForeignKey(User,related_name='complaint-user')
    category = models.ForeignKey(Category)
    #locality = models.CharField(max_length=200)
    locality = models.ForeignKey(Location)
    address = models.CharField(max_length=2000)
    date_entered = models.DateTimeField(auto_now_add=True)
    date_resolved = models.DateTimeField(null=True)
    upvotes = models.IntegerField(default=0)
    photo = models.CharField(max_length=2000)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    status_choices = (
        ('C', 'Created'),
        ('A', 'Acknowledged'),
        ('R', 'Resolved'),
        
    )
    status = models.CharField(max_length=1,choices=status_choices,default='C')
    #follower = models.ManyToManyField(User)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.title
    
class Comments(models.Model):
    complaint = models.ForeignKey(Complaint)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=2000)
    date_entered = models.DateTimeField(default=timezone.now())
    
    
class Following(models.Model):
    complaint = models.ForeignKey(Complaint)
    user = models.ForeignKey(User)
    date_followed = models.DateTimeField(auto_now_add=True)
    

    