from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("loginmodule/", include('loginmodule.urls')),
    path("", include('loginmodule.urls')),
    path("SignupApp/", include('SignupApp.urls')),
    path("BookTicketApp/", include('BookTicketApp.urls')),
    path("PaymentApp/", include('PaymentApp.urls')),
]
