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
    #return index(request)
    return redirect(str(temp1)+'/')

def loggedin(request,uname):        #blah
    return HttpResponse("<h1>redirected to "+uname+"</h1>")
#def loggedin(request):

def signup(request):
    return render(request,'home/signup.html')

def create(request):
    temp=User(username=request.POST['username'],name=request.POST['name'],password=request.POST['password'],gender=request.POST['gender'],phone=request.POST['phone'],rec_email=request.POST['email'])
    temp.save()
    return redirect('http://127.0.0.1:8000/home/login/'+temp.username+'/')