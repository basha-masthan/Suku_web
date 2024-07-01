from django.shortcuts import render,redirect
from django.http import HttpResponse
from app4.models import *
# Create your views here.
def home(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, 'registration.html')

def login(request):
    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


def adminpage(request):
    return render(request,'adminpage.html')

def modify(request):
    operation=request.GET['operation']
    name=request.GET['name']
    username=request.GET['username']
    password=request.GET['password']
    gender=request.GET['gender']
    mobile=request.GET['mobile']
    email=request.GET['email']
    desig=request.GET['desig']
    course=request.GET['course']
    graduation=request.GET['graduation']
    address=request.GET['address']
    pincode=request.GET['pincode']
    r=student.objects.get(email=email)
    if operation=="update":
        r.name=name
        r.username=username
        r.password=password
        r.gender=gender
        r.mobile=mobile
        r.email=email
        r.desig=desig
        r.course=course
        r.graduation=graduation
        r.address=address
        r.pincode=pincode
        r.save()
    else:
        student.delete(r)
    users=student.objects.all()
    return render(request,'viewusers.html',{"users":users})

def viewusers(request):
    users=student.objects.all()
    return render(request,'viewusers.html',{"users":users})

def doregister(request):
    roll = request.GET['roll']
    n1=request.GET['name1']
    n2=request.GET['name2']
    n3 = request.GET['name3']
    username=request.GET['username']
    password=request.GET['password']
    gender=request.GET['gender']
    mobile=request.GET['mobile']
    email=request.GET['email']
    dept = request.GET['dept']

    name = n1 +" "+ n2 +" "+ n3

    r=student()
    r.roll = roll
    r.name=name
    r.username=username
    r.password=password
    r.gender=gender
    r.mobile=mobile
    r.email=email
    r.dept = dept 
    r.save()
    return render(request, 'login.html')


def logincheck(request):
    username=request.GET['uname']
    password=request.GET['pwd']
    r=None
    try:
        r = Std.objects.get(roll=username)
        request.session['roll']=r.roll
    except Exception as ex:
        r=student.objects.get(username=username, password=password)
        request.session['roll']=r.roll
    return redirect('/userpage')
    # return render(request, 'home.html')

def userpage(request):
    roll=request.session['roll']
    try:
        r=Std.objects.get(roll=roll)
    except Exception as ex:
        r=student.objects.get(roll=roll)
    return render(request,'userpage.html',{"usr":r})



from django.contrib.auth import logout
def logout_1(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/login/')  # Replace 'login' with the name of your login URL pattern
