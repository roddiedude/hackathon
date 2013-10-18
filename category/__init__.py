from category.models import Category
import category.models
from django.db.models.signals import post_syncdb

def my_callback(sender, **kwargs):
    try:
        category = Category.objects.get(name__exact="Sewage")
    except Category.DoesNotExist:
        category = Category.objects.create()
        category.name = "Sewage"        
        category.save();
        
    try:
        category = Category.objects.get(name__exact="Drainage")
    except Category.DoesNotExist:
        category = Category.objects.create()
        category.name = "Drainage"        
        category.save();
    
    try:
        category = Category.objects.get(name__exact="Potholes")
    except Category.DoesNotExist:
        category = Category.objects.create()
        category.name = "Potholes"        
        category.save();
        
    try:
        category = Category.objects.get(name__exact="Water")
    except Category.DoesNotExist:
        category = Category.objects.create()
        category.name = "Water"        
        category.save();
   
    
post_syncdb.connect(my_callback, sender= category.models)