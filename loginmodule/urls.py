''' /loginmodule/urls.py '''

from loginmodule.views import *
#from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns=[
    path("",home),
    path("home/",home),
    path("login/",login),
    path("logout/",logout),
    path("auth/",auth_view),
    path("aboutus/",aboutus),
]