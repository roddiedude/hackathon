from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from category.models import Category
from ward.models import Ward
from complaint.models import Complaint
from department.models import Department
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
            
class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        
class WardResource(ModelResource):    
    class Meta:
        queryset = Ward.objects.all()
        resource_name = 'ward'                

class ComplaintResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    category = fields.ForeignKey(CategoryResource, 'category')
    filtering = {
        'user': ALL_WITH_RELATIONS,
    }
    
    class Meta:
        queryset = Complaint.objects.all()
        resource_name = 'complaint'

class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'department'       