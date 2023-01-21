''' /SignupApp/urls.py '''

from SignupApp.views import *
from django.urls import path

urlpatterns=[
	path("signup/",signup),
	path("adduserinfo/",adduserinfo),
]