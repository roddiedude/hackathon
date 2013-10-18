from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from category.models import Category
from ward.models import Ward
from complaint.models import Complaint, Comments
from department.models import Department
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization



class UserResource(ModelResource):    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
 

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()
        
class WardResource(ModelResource):    
    class Meta:
        queryset = Ward.objects.all()
        resource_name = 'ward'
        authorization = Authorization()                

class ComplaintResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    category = fields.ForeignKey(CategoryResource, 'category')
    filtering = {
        'user': ALL_WITH_RELATIONS,
    }
    
    class Meta:
        queryset = Complaint.objects.all()
        resource_name = 'complaint'
        authorization = Authorization()

class DepartmentResource(ModelResource):
    class Meta:
        queryset = Department.objects.all()
        resource_name = 'department'
        authorization = Authorization()       

class CommentResource(ModelResource):
    complaint = fields.ForeignKey(ComplaintResource, 'complaint')
    
    class Meta:
        queryset = Comments.objects.all()
        resource_name = 'comment'
        authorization = Authorization()