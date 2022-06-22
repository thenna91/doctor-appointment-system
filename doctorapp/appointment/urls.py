from django.urls import path,include
from .views import doctorlist,listappoinment,listappoinmentbydoctor,deleteappointment,createappointment

urlpatterns = [
    path('', doctorlist.as_view()),
    path('physicians/', doctorlist.as_view()),
    path('listappoinment/<int:id>',listappoinmentbydoctor.as_view()),
    path('listappoinment/',listappoinment.as_view()),
    path('deleteappointment/<int:pk>',deleteappointment.as_view()),
    path('newappointment/',createappointment.as_view()),
]