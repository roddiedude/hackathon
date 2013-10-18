from location.models import Location
import location.models
from django.db.models.signals import post_syncdb

def my_callback(sender, **kwargs):
    try:
        location = Location.objects.get(name__exact="Guindy")
    except Location.DoesNotExist:
        location = Location.objects.create()
        location.name = "Guindy"        
        location.save();
    
    try:
        location = Location.objects.get(name__exact="Alwarpet")
    except Location.DoesNotExist:
        location = Location.objects.create()
        location.name = "Alwarpet"        
        location.save();
    
    
    try:
        location = Location.objects.get(name__exact="Adyar")
    except Location.DoesNotExist:
        location = Location.objects.create()
        location.name = "Adyar"        
        location.save(); 
   
    try:
        location = Location.objects.get(name__exact="Saidapet")
    except Location.DoesNotExist:
        location = Location.objects.create()
        location.name = "Saidapet"        
        location.save(); 
    
post_syncdb.connect(my_callback, sender= location.models)