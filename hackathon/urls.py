from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


from tastypie.api import Api
from hackathon.api import *

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(UserInfoResource())
v1_api.register(CategoryResource())
v1_api.register(LocationResource())
v1_api.register(WardResource())
v1_api.register(ComplaintResource())
v1_api.register(DepartmentResource())
v1_api.register(CommentResource())
v1_api.register(FollowingResource())
        
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hackathon.views.home', name='home'),
    # url(r'^hackathon/', include('hackathon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^complaint/', include('complaint.urls', namespace="complaint")),
    
    url(r'', include('accounts.urls', namespace="accounts")),
    
    url(r'^accounts/', include('accounts.urls', namespace="accounts")),
    
    (r'^api/', include(v1_api.urls)),
    
    url(r'^accounts/login/', 'accounts.views.home'),
)
