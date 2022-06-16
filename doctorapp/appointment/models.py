from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone

# Create your models here.

def future(value):
    current_time = timezone.now()
    if value < current_time:
        raise ValidationError('Please provide valid Future Data')

class Doctor(models.Model):
    firstname = models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    def __str__(self):
        return self.firstname


class Doctorappointment(models.Model):
    doctor=models.ForeignKey(Doctor,related_name='doctorappointment',on_delete=models.DO_NOTHING )
    patient_firstname=models.CharField(max_length=20)
    patient_lastname=models.CharField(max_length=20)
    appointment_time=models.DateTimeField(validators=[future])
    visit_choices = (
        ('New-Patient','New-Patient'),
        ('Follow-up','Follow-up'),
    )
    visit_type=models.CharField(max_length=20,choices=visit_choices,default = 'New-Patient')
    
    def __str__(self):
        return self.patient_firstname
    
