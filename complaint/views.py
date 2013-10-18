from django.shortcuts import render

def index(request):
    return render(request, 'children/viewcomplaints.html')

def addcomplaint(request):
    return render(request, 'complaint/add-complaint.html')## Create your views here.

def partial_add_complaint(request):
    return render(request, 'complaint/partials/add-complaint.html')

def partial_my_complaints(request):
    return render(request, 'complaint/partials/my-complaints.html')