from django.conf.urls import patterns, url

from complaint import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='complaints'),
     url(r'^addcomplaint/$', views.addcomplaint, name='addcomplaint'),
     url(r'^add-complaint$', views.partial_add_complaint, name='add-complaint'),
     url(r'^my-complaints$', views.partial_my_complaints, name='my-complaints'),
        
)