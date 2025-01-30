from django.contrib import admin
from .models import Announcement, Household, Resident, Complaint

admin.site.register(Announcement)
admin.site.register(Household)
admin.site.register(Resident)

admin.site.register(Complaint)