from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import simplejson
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from hackathon.api import *
from department.models import Department


def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('accounts:landing'))
    
    return render(request, 'accounts/homepage.html')

@login_required
def landing(request):
    usr = request.user
    try:
        department = Department.objects.get(user = usr)
    except Department.DoesNotExist:        
        return render(request, 'accounts/landing.html')                    
    else:
        return render(request, 'accounts/admin-landing.html')

@login_required
def admin_landing(request):
    return render(request, 'accounts/admin-landing.html')

@login_required
def partial_edit(request):
    return render(request, 'accounts/partials/edit.html')

@csrf_exempt
def login(request):
    response = {}
       

    if request.method == 'POST':
        userjson = simplejson.loads(request.raw_post_data)
        
        try:
            """"TODO: check if user already exists"""
            usr = authenticate(username=userjson['userName'], password=userjson['password'])
            try:
                department = Department.objects.get(user = usr)
            except Department.DoesNotExist:
                if usr.is_active:
                    auth_login(request, usr)
                    response['message'] = 'success'
                    response['redirect'] = reverse('accounts:landing')
                    return HttpResponse(simplejson.dumps(response))            
            else:
                if usr.is_active:
                    auth_login(request, usr)
                    response['message'] = 'success'
                    response['redirect'] = reverse('accounts:admin_landing')
                    return HttpResponse(simplejson.dumps(response))
        except User.DoesNotExist:
            response['message'] = 'Unknown username or password'    
            return HttpResponse(simplejson.dumps(response))
                
    response['message'] = 'Unknown username or password'    
    return HttpResponse(simplejson.dumps(response))

@login_required
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('accounts:homepage'))

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

@login_required      
def userInfo(request):
    userResource = UserInfoResource()
    usr = request.user
    
    userInfo = get_object_or_404(UserInfo, user=usr);

    bundles = []    
    bundle = userResource.build_bundle(obj=userInfo, request=request)
    
    bundles.append(userResource.full_dehydrate(bundle))
    json = userResource.serialize(None, bundles, "application/json")
    return HttpResponse(json, content_type='json')


def locality(request):
    return render(request, 'accounts/locality.html')

def editAccount(request):
    return render(request, 'accounts/editAccount.html')