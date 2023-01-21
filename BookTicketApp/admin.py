''' /BookTicketApp/admin.py '''

from django.contrib import admin
from .models import PackageDetails,TMSBooking,feedback

admin.site.register(PackageDetails)
admin.site.register(TMSBooking)
admin.site.register(feedback)