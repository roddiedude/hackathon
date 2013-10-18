from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from hackathon.api import *


def home(request):
    return render(request, 'accounts/homepage.html')

@login_required
def landing(request):
    return render(request, 'accounts/landing.html')

@login_required
def partial_edit(request):
    return render(request, 'accounts/partials/edit.html')

@csrf_exempt
def login(request):
    response = {}    

    if request.method == 'POST':
        userjson = simplejson.loads(request.raw_post_data)
        
        """"TODO: check if user already exists"""
        user = authenticate(username=userjson['userName'], password=userjson['password'])
        if user is not None:
            # the password verified for the user
            if user.is_active:
                auth_login(request, user)
                response['message'] = 'success'
                response['redirect'] = reverse('accounts:landing')
                return HttpResponse(simplejson.dumps(response))
                
    response['message'] = 'Unknown username or password'    
    return HttpResponse(simplejson.dumps(response))

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('accounts:'))

@csrf_exempt
def signup(request):
    response = {}        

    if request.method == 'POST':
        userjson = simplejson.loads(request.raw_post_data)            

        try:
            u = User.objects.get(username__exact=userjson['userName'])
        except User.DoesNotExist:
            user = User.objects.create_user(userjson['userName'],userjson['email'], userjson['password']);
            user.last_name = userjson['lastName']
            user.first_name = userjson['firstName']
            user.save();
            
            user = authenticate(username=userjson['userName'], password=userjson['password'])
            auth_login(request, user)
            
            response['message'] = 'success'
            response['redirect'] = reverse('accounts:landing')
            return HttpResponse(simplejson.dumps(response))
        else:
            
            response['message'] = 'User already present'
            return HttpResponse(simplejson.dumps(response))

    response['message'] = 'failure'
    return HttpResponse(simplejson.dumps(response))

def partial_sign_up(request):
    return render(request, 'accounts/partials/sign-up.html')

def partial_home(request):
    return render(request, 'accounts/partials/home.html')
       
@login_required      
def info(request):
    userResource = UserResource()
    usr = request.user

    bundles = []    
    bundle = userResource.build_bundle(obj=usr, request=request)
    
    bundles.append(userResource.full_dehydrate(bundle))
    json = userResource.serialize(None, bundles, "application/json")
    return HttpResponse(json, content_type='json')

