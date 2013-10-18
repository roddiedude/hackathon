from django.conf.urls import patterns, url

from accounts import views

urlpatterns = patterns('',
     url(r'^$', views.home, name='home'),     
     url(r'^login$', views.login, name='login'),
     url(r'^landing$', views.landing, name='landing'),          
     url(r'^logout', views.logout, name='logout'),
)