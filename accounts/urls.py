from django.conf.urls import patterns, include, url

from accounts import views

urlpatterns = patterns('',
     url(r'^$', views.home, name='home'),     
     url(r'^login$', views.login, name='login'),
     url(r'^landing$', views.landing, name='landing'),          
     url(r'^logout', views.logout, name='logout'),
     url(r'^signup', views.signup, name='signup'),
     url(r'^sign-up$', views.partial_sign_up, name='sign-up'),
     url(r'^home$', views.partial_home, name='home'),
)