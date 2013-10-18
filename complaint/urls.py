from django.conf.urls import patterns, url

from complaint import views

urlpatterns = patterns('',
     #url(r'^$', views.index, name='complaints'),
     url(r'^addcomplaint/$', views.addcomplaint, name='addcomplaint'),
     url(r'^$', views.mycomplaints, name='mycomplaints'),
     url(r'^complaintsassigned/$', views.complaints_in_myplate, name='complaints_in_my_plate'),
     url(r'^add-complaint$', views.partial_add_complaint, name='add-complaint'),
     url(r'^detail/(?P<complaint_id>\d+)/$', views.detail, name='detail'),
     url(r'^upvote/(?P<complaint_id>\d+)/$', views.upvote, name='upvote'),
)