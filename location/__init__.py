from location.models import Location
import location.models
from django.db.models.signals import post_syncdb

def create_location(name):
    try:
        location = Location.objects.get(name__exact=name)
    except Location.DoesNotExist:
        location = Location.objects.create()
        location.name = name        
        location.save();

def my_callback(sender, **kwargs):
    create_location("Tondiarpet")
    create_location("Basin Bridge")
    create_location("Pulianthope")
    create_location("Ayanavaram")
    create_location("Kilpauk")
    create_location("Ice House")
    create_location("Nungambakkam")
    create_location("Kodambakkam")
    create_location("Saidapet")
    create_location("Adyar")
    
post_syncdb.connect(my_callback, sender= location.models)