from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User,User_id
# Create your views here.

def index(request):
    a={}
    return render(request,'home/index.html',a)

def login(request):
    temp1=request.POST['uname']
    temp2=request.POST['psw']
    my_object=get_object_or_404(User,username=temp1,password=temp2)
    obj=open("login.txt","w")
    obj.write(my_object.username)
    obj.close()
    #return index(request)

    return redirect(str(temp1)+'/')

def loggedin(request,uname):        #blah

    obj=open("login.txt","r+")
    strin=obj.read()
    obj.close()
    if strin==uname:
        print "okay"

        my_object=get_object_or_404(User,username=uname)
        a=my_object.name
        b={}
        b['name']=a
        return render(request,'home/welcome.html',b)
    else:
        return HttpResponse("<h1>YOU ARE NOT AUTHORIZED TO DO SO<h1>")
    #return HttpResponse("<h1>redirected to "+b['name']+"</h1>")


def signup(request):
    return render(request,'home/signup.html')

def create(request):
    temp=User(username=request.POST['username'],name=request.POST['name'],password=request.POST['password'],gender=request.POST['gender'],phone=request.POST['phone'],rec_email=request.POST['email'])
    temp.save()
    obj=open("login.txt","w")
    obj.write(temp.username)
    obj.close()
    return redirect('http://127.0.0.1:8000/home/login/'+temp.username+'/')

def auth(request):
    obj=open("hello.txt","w")
    obj.write(request.POST['uname'])
    obj.close()

    return HttpResponse(request.POST['uname'])

