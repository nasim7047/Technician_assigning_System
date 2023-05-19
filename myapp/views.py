from django.shortcuts import render,redirect
from .models import Users,Proffesional,Servicesreq
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
# import requests



# Create your views here.
def Userreg(request):
    if request.method=="POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phone")
        password=request.POST.get("password")
        

        details = Users(name=name,address=address,email=email,phone=phonenumber,password=password)
        
        details.save()
        return redirect("../login")
    return render(request,"sign.html")


def prof(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        # dob=request.POST.get("dob")
        qualification=request.POST.get("qualification")
        work_experiece=request.POST.get("work")
        password=request.POST.get("password")

        obj = Proffesional(name=name,address=address,email=email,phone=phone,qualification=qualification,work_experiece=work_experiece,password=password)
        obj.save()
        return redirect("../prologin")
    return render(request,"home.html")

def Servicereq(request):
    if request.method=="POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phonenumber = request.POST.get("phone")
        services = request.POST.get("service")

        servdetails = Servicesreq(name=name,address=address,email=email,phone=phonenumber,services=services)       
        servdetails.save()
        return redirect("../thank")
    return render(request,"sign.html")

def home(request):
    return render(request,'home.html')
def login(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        #user = authenticate(request,email=email,password=password)
        # print(email,password)
        try:
            if Users.objects.filter(email=email,password=password):
                #login(request,user)
                return redirect("../afterlogin")
            else:
                return HttpResponse("Username or Password is not valid!!!")
        except Exception as e:
            return HttpResponse(e)      
    return render(request,'login.html')


def signup(request):
    return render(request,'signup.html')
def con(request):
    return render(request,'contact.html')
def reg(request):
    return render(request,'register.html')
def servicesignup(request):
    return render(request,'services.html')
def thanks(request):
    return render(request,'thank.html')
def professionalogin(request):
    if request.method=="POST":
        email = request.POST.get("email")
        password = request.POST.get("pass")
        try:
            if Proffesional.objects.filter(email=email,password=password):
                return redirect("../afterprlogin")
            else:
                return HttpResponse("Username or Password is not valid!!!")
        except Exception as e:
            return HttpResponse(e)
    return render(request,'prof_login.html')

def thanks(request):
    return render(request,'thank.html')  
def adminlog(request):
    return render(request,'admin login.html')       

def profshow(request):
    showprtab=Servicesreq.objects.all()
    return render(request,'task.html',{'table':showprtab})
def show(request):
    showtab=Servicesreq.objects.all()
    return render(request,'showuser.html',{'table':showtab})

def aflog(request):
    return render(request,'after_user_login.html')
def afprlog(request):
    return render(request,'after_prof_login.html')



