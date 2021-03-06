from django.conf.urls import patterns, url
from complaint import views

urlpatterns = patterns('',
     url(r'^addcomplaint/$', views.addcomplaint, name='addcomplaint'),
     url(r'^$', views.mycomplaints, name='mycomplaints'),
     url(r'^all-complaints/$', views.complaints_in_myplate, name='complaints_in_my_plate'),
     url(r'^recent-complaints/$', views.recent_complaints, name='recent_complaints'),
     url(r'^top-complaints/$', views.top_complaints, name='top_complaints'),
     url(r'^localcomplaints/$', views.complaints_in_mylocality, name='complaints_in_my_locality'),
     url(r'^(?P<complaint_id>\d+)/followers$', views.followers_of_my_complaints, name='followers_of_my_complaints'),     
     url(r'^localcomplaints/$', views.complaints_in_mylocality, name='complaints_in_my_locality'),
     url(r'^add-complaint$', views.partial_add_complaint, name='add-complaint'),
     url(r'^my-complaints$', views.partial_my_complaints, name='my-complaints'),
     url(r'^detail/(?P<complaint_id>\d+)/$', views.detail, name='detail'),
     url(r'^upvote/(?P<complaint_id>\d+)/$', views.upvote, name='upvote'),
     url(r'^comments/(?P<complaint_id>\d+)/$', views.comment, name='comment')          
)
        


