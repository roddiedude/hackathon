from category.models import Category
import category.models
from django.db.models.signals import post_syncdb

def create_category(name):
    try:
        category = Category.objects.get(name__exact=name)
    except Category.DoesNotExist:
        category = Category.objects.create()
        category.name = name      
        category.save();

def my_callback(sender, **kwargs):
    create_category("Bridges")
    create_category("Building")
    create_category("Education")
    create_category("Electrical")
    create_category("Finance")
    create_category("Health")
    create_category("Land & Estates")
    create_category("Law & Order")
    create_category("Mechanical Engineering")
    create_category("Metro Water")
    create_category("Parks")
    create_category("Revenue")
    create_category("Road")
    create_category("Small Savings")
    create_category("Solid Waste Management")
    create_category("Storm Water Drainage")
    create_category("Town Planning")
    create_category("Traffic")   
    
post_syncdb.connect(my_callback, sender= category.models)