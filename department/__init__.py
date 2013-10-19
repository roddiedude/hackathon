from department.models import Department
import department.models
from django.db.models.signals import post_syncdb
from category.models import Category
from django.contrib.auth.models import User

def my_callback(sender, **kwargs):
    try:
        department = Department.objects.get(department_name__exact="Chennai Metro Water")
    except Department.DoesNotExist:
        u = User.objects.get(username__exact="chennaimetrowater")
        department = Department(user=u)
        department.department_name = "Chennai Metro Water"
        department.website = "http://www.chennaimetrowater.tn.nic.in/"
        department.person_in_charge = "Water Ministry, Chennai Corporation"
        department.contact_numbers = "45674567"
        department.working_hours_days = " Mon-Fri 9AM-5PM"
        department.save();
        
        category = Category.objects.get(name__exact="Sewage")
        
        department.categories.add(category)
        
        category = Category.objects.get(name__exact="Drainage")
        department.categories.add(category)
        department.save();

    
post_syncdb.connect(my_callback, sender= department.models)