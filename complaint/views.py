from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from complaint.models import Complaint
from complaint.models import Following
from category.models import Category
from department.models import Department
from location.models import Location
from accounts.models import UserInfo
from django.core import serializers
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from complaint.models import Complaint
from category.models import Category
from department.models import Department
from django.core import serializers
from hackathon.api import *


def index(request):
    return render(request, 'children/viewcomplaints.html')

def addcomplaint(request):
    return render(request, 'complaint/add-complaint.html')

def mycomplaints(request):
    complaint = ComplaintResource()
    usr = request.user
    complaints=get_list_or_404(Complaint,user=usr)

    bundles = []
    for obj in complaints:
        bundle = complaint.build_bundle(obj=obj, request=request)
        bundles.append(complaint.full_dehydrate(bundle, for_list=True))

    list_json = complaint.serialize(None, bundles, "application/json")

    return HttpResponse(list_json, content_type='json')

def complaints_in_myplate(request):
    complaint = ComplaintResource()
    usr = request.user
    dpt = get_object_or_404(Department,user=usr)
    #categories = get_list_or_404(Category,department=dpt)
    categories = Department.objects.all().filter(pk = dpt.id)
    complaints = []    
    for cat in categories:
        comps =get_list_or_404(Complaint,category=cat)
        for comp in comps:
            complaints.append(comp)
    bundles = []
    for obj in complaints:
        bundle = complaint.build_bundle(obj=obj, request=request)
        bundles.append(complaint.full_dehydrate(bundle, for_list=True))

    list_json = complaint.serialize(None, bundles, "application/json")
    return HttpResponse(list_json, content_type='json')


def complaints_in_mylocality(request):
    complaint = ComplaintResource()
    usr = request.user
    usrinfo = get_object_or_404(UserInfo,user=usr)
    loc = usrinfo.location
    complaints = get_list_or_404(Complaint,locality=loc)   
    bundles = []
    for obj in complaints:
        bundle = complaint.build_bundle(obj=obj, request=request)
        bundles.append(complaint.full_dehydrate(bundle, for_list=True))

    list_json = complaint.serialize(None, bundles, "application/json")
    return HttpResponse(list_json, content_type='json')


def followers_of_my_complaints(request,complaint_id):
    following = FollowingResource()
    
    cmp = Complaint.objects.get(pk=complaint_id)
    followers = get_list_or_404(Following,complaint=cmp)   
       
    bundles = []
    for obj in followers:
        bundle = following.build_bundle(obj=obj, request=request)
        bundles.append(following.full_dehydrate(bundle, for_list=True))

    list_json = following.serialize(None, bundles, "application/json")
    return HttpResponse(list_json, content_type='json')

def my_complaints_followercount(request,complaint_id):
    following = FollowingResource()
    followers = followers_of_my_complaints(complaint_id)
    cnt = followers.count
    following.build_bundle(obj=cnt, request=request)
    


def partial_add_complaint(request):
    return render(request, 'complaint/partials/add-complaint.html')

def partial_my_complaints(request):
    return render(request, 'complaint/partials/my-complaints.html')







    

def upvote(request, complaint_id):
    complaint = get_object_or_404(Complaint, pk=complaint_id)
    complaint.upvotes = complaint.upvotes + 1
    complaint.save()
    return HttpResponse("")

def detail(request, complaint_id):
    return render(request, 'complaint/detail.html',  {'complaint_id':complaint_id})


