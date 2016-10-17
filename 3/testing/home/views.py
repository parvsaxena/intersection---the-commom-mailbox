from django.shortcuts import render,redirect
from django.http import HttpResponse
from oauth2client.client import OAuth2WebServerFlow
import httplib2
from apiclient.discovery import build
from oauth2client.file import Storage
from apiclient import errors

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




def index(request):
    flow = OAuth2WebServerFlow(client_id='591249218571-2pf4rg5fctvbb5bmui2m9vj4q46denrq.apps.googleusercontent.com',client_secret='uJtle-AJU-VahuYmDuEgW9cU',scope='https://mail.google.com/',redirect_uri='http://127.0.0.1:8000/home/welcome/',)
    flow.params['access_type'] = 'offline'
    flow.params['approval_prompt'] = 'force'
    auth_uri = flow.step1_get_authorize_url()
    return redirect(auth_uri)


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

    #msg=ListMessagesMatchingQuery(service,'archit969@gmail.com')
    #print msg
    return HttpResponse(code)