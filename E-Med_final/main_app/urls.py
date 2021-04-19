from django.urls import path , re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('about', views.about , name='about'),
    path('mdoctor', views.mdoctor , name='mdoctor'),
    path('contact', views.contact , name='contact'),
    path('viewhospital', views.viewhospital , name='viewhospital'),
    path('viewremedy', views.viewremedy , name='viewremedy'),
    


    path('patient_ui', views.patient_ui , name='patient_ui'),
    path('checkdisease', views.checkdisease, name="checkdisease"),
    path('pviewprofile/<str:patientusername>', views.pviewprofile , name='pviewprofile'),
    path('pconsultation_history', views.pconsultation_history , name='pconsultation_history'),
    path('consult_a_doctor', views.consult_a_doctor, name='consult_a_doctor'),
    path('related_hospital', views.related_hospital , name='related_hospital'),
    path('home_remedy', views.home_remedy , name='home_remedy'),
    path('make_consultation/<str:doctorusername>', views.make_consultation , name='make_consultation'),


    path('dconsultation_history', views.dconsultation_history , name='dconsultation_history'),
    path('dviewprofile/<str:doctorusername>', views.dviewprofile , name='dviewprofile'),
    path('doctor_ui', views.doctor_ui , name='doctor_ui'),
    
    path('hospital/<int:hospital_id>', views.hospital , name='hospital'),
    path('remedy/<int:remedy_id>', views.remedy , name='remedy'),
    path('consultationview/<int:consultation_id>', views.consultationview , name='consultationview'),


    
    path('post', views.post, name='post'),
    path('chat_messages', views.chat_messages, name='chat_messages'),
    


]  
