from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import User,User_id,Mail

from oauth2client.client import OAuth2WebServerFlow
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from apiclient import errors
import base64
import email

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
    #enter the sent email into hello.txt

    obj=open("hello.txt","w")
    obj.write(request.POST['uname'])
    obj.close()

    # checking and making entry for it in user_id object

    ob=User_id.objects.filter(email_id=request.POST['uname'])
    if ob:
        print "exists"
    else:
        print "does not exist"
        obj=open("login.txt","r+")
        strin=obj.read()
        obj.close()
        temp=User.objects.get(username=strin)       #user object
        temp1=User_id(user_name=temp,email_id=request.POST['uname']) #user_id object created
        temp1.save()



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




def GetMessage(service, user_id, msg_id):
  """Get a Message with given ID.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id).execute()

    #print ('Message snippet: %s' % message['snippet'])

    return message
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)



def GetMimeMessage(service, user_id, msg_id):
  """Get a Message and use it to create a MIME Message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    msg_id: The ID of the Message required.

  Returns:
    A MIME Message, consisting of data from Message.
  """
  try:
    message = service.users().messages().get(userId=user_id, id=msg_id,
                                             format='raw').execute()

    #print ('Message snippet: %s' % message['snippet'])

    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))

    mime_msg = email.message_from_string(msg_str)

    return mime_msg
  except errors.HttpError, error:
    print ('An error occurred: %s' % error)


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


    #retrieving user_id
    obj=open("hello.txt","r+")
    strin=obj.read()
    obj.close()
    #print strin


    msg1=ListMessagesMatchingQuery(service,strin)
    #print msg

    for i in range(0,30):
        mime = GetMimeMessage(service,strin,msg1[i]['id'])
        msg = GetMessage(service,strin,msg1[i]['id'])
        #print mime
        print msg['id']
        print mime['Date']
        print msg['snippet'].encode("utf-8")
        print msg['internalDate']
        print mime['Subject']
        print mime['From']
        s = str(mime)
        t = str(mime)
        t1=""
        t2=""
        html=""
        try:
            t1 = t.split('Content-Type: text/plain;')[1]
            t2 = t1.split('Content-Type: text/html;')[0]    #plain text
        except IndexError:
            print "Plaint text doesnt exist"
        try:
            s1 = s.split('<body>')[1]
            s2 = s1.split('</body>')[0]
            html = "<body>"+s2+"</body>"
        except IndexError:
            print "HTML doesnt exist"
        ob=User_id.objects.get(email_id=strin)
        if ob:
            temp=Mail(user_n=ob,sender=mime['From'],msg_id=msg['id'],html_body=html,plain_body=t2,date=mime['Date'],snippet=msg['snippet'],subject=mime['Subject'],intern=msg['internalDate'])
            temp.save()
        else:
            print "error"

    #print msg
    return render(request,'home/welcome.html')