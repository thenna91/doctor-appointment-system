from django.shortcuts import render

# Create your views here.
from rest_framework.generics import  ListAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView

from .models import Doctor,Doctorappointment
from .serializers import doctorSerializer,AppointmentSerializer,DeleteAppointmentSerializer,CreateAppointmentSerializer

class doctorlist(ListCreateAPIView):
    queryset=Doctor.objects.all()
    serializer_class=doctorSerializer

class listappoinment(ListAPIView):
    queryset=Doctor.objects.all()
    serializer_class=AppointmentSerializer

class listappoinmentbydoctor(ListAPIView):
    serializer_class=AppointmentSerializer
    def get_queryset(self):
        doctor_id=self.kwargs['id']
        return Doctor.objects.filter(id=doctor_id)

class deleteappointment(RetrieveUpdateDestroyAPIView):
      queryset=Doctorappointment.objects.all()
      serializer_class=DeleteAppointmentSerializer
      lookup_field = 'pk'

class createappointment(ListCreateAPIView):
     serializer_class=CreateAppointmentSerializer
     queryset=Doctorappointment.objects.all()


