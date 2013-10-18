from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from category.models import Category
from complaint.models import Following
from accounts.models import UserInfo
from ward.models import Ward
from location.models import Location
from complaint.models import Complaint, Comments
from department.models import Department
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization



class UserResource(ModelResource):    
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
 
class UserInfoResource(ModelResource):    
    class Meta:
        queryset = UserInfo.objects.all()
        resource_name = 'userinfo'
        authorization = Authorization()

class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'category'
        authorization = Authorization()

class FollowingResource(ModelResource):
    class Meta:
        queryset = Following.objects.all()
        resource_name = 'following'
        authorization = Authorization()
        
class WardResource(ModelResource):    
    class Meta:
        queryset = Ward.objects.all()
        resource_name = 'ward'
        authorization = Authorization() 
        
class LocationResource(ModelResource):    
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        authorization = Authorization()                   

class ComplaintResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    category = fields.ForeignKey(CategoryResource, 'category')
    locality = fields.ForeignKey(LocationResource, 'locality')    
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
