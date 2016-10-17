from django.conf.urls import url
from . import views


app_name='home'

urlpatterns = [
    #home/
    url(r'^$', views.index,name='index'),
    #home/login
    url(r'^login/$',views.login,name='login' ),
    #home/login/<uname>
    url(r'^login/(?P<uname>[a-zA-Z0-9._]+)/$',views.loggedin,name='loggedin' ),   #blah
    #home/signup
    url(r'^signup/$',views.signup,name='signup'),
    #home/create
    url(r'^create/$',views.create,name='create'),
    #home/auth
    url(r'^auth/$',views.auth,name='auth'),
    #get redirected by google to home/welcome
    url(r'^welcome/$',views.wel,name="wel")

]
