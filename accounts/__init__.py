from django.contrib.auth.models import User
import accounts.models
from django.db.models.signals import post_syncdb

def my_callback(sender, **kwargs):
    try:
        u = User.objects.get(username__exact="priyas")
    except User.DoesNotExist:
        user = User.objects.create_user("priyas","priyas@email.com", "test");
        user.last_name = "Sebastian"
        user.first_name = "Priya"
        user.save();
    
    try:
        u = User.objects.get(username__exact="nages")
    except User.DoesNotExist:
        user = User.objects.create_user("nages","nages@email.com", "test");
        user.last_name = "Sokkayarajan"
        user.first_name = "Nageswaran"
        user.save();
    
    try:
        u = User.objects.get(username__exact="karthikeyan")
    except User.DoesNotExist:
        user = User.objects.create_user("karthikeyan","karthikeyank@email.com", "test");
        user.last_name = "Kumar"
        user.first_name = "Karthikeyan"
        user.save();
    
    try:
        u = User.objects.get(username__exact="deepanm")
    except User.DoesNotExist:
        user = User.objects.create_user("deepanm","deepan@email.com", "test");
        user.last_name = "Manohar"
        user.first_name = "Deepan"
        user.save();
    
    try:
        u = User.objects.get(username__exact="iswaryar")
    except User.DoesNotExist:
        user = User.objects.create_user("iswaryar","iswaryar@email.com", "test");
        user.last_name = "Rajagopal"
        user.first_name = "Iswarya"
        user.save();
        
    try:
        u = User.objects.get(username__exact="vgp")
    except User.DoesNotExist:
        user = User.objects.create_user("vgp","vgp@email.com", "test");
        user.last_name = "Pandian"
        user.first_name = "Varaguna"
        user.save();
        
    try:
        u = User.objects.get(username__exact="chennaimetrowater")
    except User.DoesNotExist:
        user = User.objects.create_user("chennaimetrowater","chennaimetrowater@email.com", "test");
        user.last_name = "Metro Water"
        user.first_name = "Chennai Metro Water"
        user.save();
    
post_syncdb.connect(my_callback, sender= accounts.models)