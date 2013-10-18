from django.db import models
#from department.models import Department

# Create your models here.
class Category(models.Model):    
    name = models.CharField(max_length=200)
    #department = models.ManyToManyField(Department)
    
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name