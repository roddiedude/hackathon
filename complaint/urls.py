from django.conf.urls import patterns, url

from complaint import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='complaints'),
     url(r'^addcomplaint/$', views.addcomplaint, name='addcomplaint'),
        
)