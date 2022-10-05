from datetime import datetime
from django.shortcuts import render,HttpResponse
from app.models import Contact


# Create your views here.
def index(request):
    '''return HttpResponse("this is homepage")'''
    return render(request,"index.html")

def home(request):
    return render(request,"home.html")

def about(request):
    return about(request,"about.html")

def contact(request):
    return contact(request,"about.html")
    

def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,Phone=Phone,desc=desc,date =datetime.today())
        contact.save()
    
    return render(request,'contact.html')

def home(request):
    return render(request,'home.html')

def Photos(request):
    return render(request,'Photos.html')




