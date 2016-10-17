from django.conf.urls import url
from . import views


app_name='home'

urlpatterns = [
    #home/
    url(r'^$', views.index,name='index'),
    #home/login
    url(r'^login/$',views.login,name='login' ),
    url(r'^login/blah/$',views.loggedin,name='loggedin' ),
    #home/signup
    url(r'^signup/$',views.signup,name='signup'),
    #home/create
    url(r'^create/$',views.create,name='create')
]
