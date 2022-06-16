from operator import ne
from rest_framework import serializers

from .models import Doctor,Doctorappointment

import datetime

class doctorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields = "__all__"

class DoctorAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctorappointment
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    doctorappointment = DoctorAppointmentSerializer(many=True, read_only=True)
    class Meta:
        model=Doctor
        fields = ['id','firstname', 'lastname', 'doctorappointment']

class DeleteAppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Doctorappointment
        fields = "__all__"

class CreateAppointmentSerializer(serializers.ModelSerializer):  
    class Meta:
        model=Doctorappointment
        fields = "__all__"
    def validate(self, data):
        year = data['appointment_time'].strftime("%Y")
        month=data['appointment_time'].strftime("%m")
        day = data['appointment_time'].strftime("%d")
        hour =data['appointment_time'].strftime("%H")
        minute =data['appointment_time'].strftime("%M")

        if minute  not in ("00","15","30","45"):
            raise serializers.ValidationError("Please provide Valid Appointment time")

        appointment_count = Doctorappointment.objects.filter(doctor=data['doctor']).filter(appointment_time__date=datetime.date(int(year),int(month),int(day))).filter(appointment_time__time=datetime.time(int(hour),int(minute))).count()
        if appointment_count >= 3:
            raise serializers.ValidationError("Appoinments already booked for this date.Please choose new date and time")
        return data



