from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User,User_id,Mail

from oauth2client.client import OAuth2WebServerFlow
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from apiclient import errors


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
    flow = OAuth2WebServerFlow(client_id='591249218571-2pf4rg5fctvbb5bmui2m9vj4q46denrq.apps.googleusercontent.com',client_secret='uJtle-AJU-VahuYmDuEgW9cU',scope='https://mail.google.com/',redirect_uri='http://127.0.0.1:8000/home/welcome/',)
    flow.params['access_type'] = 'offline'
    flow.params['approval_prompt'] = 'force'
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)
    #return HttpResponse(request.POST['uname'])






def ListMessagesMatchingQuery(service, user_id, query=''):
  """List all Messages of the user's mailbox matching the query.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    query: String used to filter messages returned.
    Eg.- 'from:user@some_domain.com' for Messages from a particular sender.

  Returns:
    List of Messages that match the criteria of the query. Note that the
    returned list contains Message IDs, you must use get with the
    appropriate ID to get the details of a Message.
  """
  try:
    response = service.users().messages().list(userId=user_id,
                                               q=query).execute()
    messages = []
    if 'messages' in response:
      messages.extend(response['messages'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().messages().list(userId=user_id, q=query,
                                         pageToken=page_token).execute()
      messages.extend(response['messages'])

    return messages
  except errors.HttpError, error:
    print 'An error occurred: %s' % error

def wel(request):
    a='hello'
    #this im my auth code
    code=request.GET['code']

    flow = OAuth2WebServerFlow(client_id='591249218571-2pf4rg5fctvbb5bmui2m9vj4q46denrq.apps.googleusercontent.com',client_secret='uJtle-AJU-VahuYmDuEgW9cU',scope='https://mail.google.com/',redirect_uri='http://127.0.0.1:8000/home/welcome/')
    flow.params['access_type'] = 'offline'
    flow.params['approval_prompt'] = 'force'
    #these are my credentials
    credentials = flow.step2_exchange(code)
    #Use the authorize() function of the Credentials class to apply necessary credential headers to all requests made by an httplib2.Http instance
    print credentials
    http = httplib2.Http()
    http = credentials.authorize(http)
    #credentials.refresh(http)
    #pass to build function
    service = build('gmail', 'v1', http=http)
    #storage
    storage = Storage('a.txt')
    storage.put(credentials)
    credentials = storage.get()
    #print credentials

    #msg=ListMessagesMatchingQuery(service,'saxena.parv23@gmail.com')
    #print msg
    return HttpResponse(code)