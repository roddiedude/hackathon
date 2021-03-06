from django.db import models
from django.contrib.auth.models import User
from category.models import Category


class Department(models.Model):
    user = models.OneToOneField(User)
    department_name = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    person_in_charge = models.CharField(max_length=200)
    contact_numbers = models.CharField(max_length=200)
    working_hours_days = models.CharField(max_length=200)
    categories = models.ManyToManyField(Category)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.department_name
     
    
    
