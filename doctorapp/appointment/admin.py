from django.contrib import admin

# Register your models here.

from .models import Doctorappointment, Doctor
admin.site.register(Doctor)
admin.site.register(Doctorappointment)