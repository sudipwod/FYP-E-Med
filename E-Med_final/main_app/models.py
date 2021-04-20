from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

from datetime import date

# Create your models here.


#user = models.OneToOneField(settings.AUTH_USER_MODEL)

class patient(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_patient = models.BooleanField(default=True)
    is_doctor = models.BooleanField(default=False)
    name = models.CharField(max_length = 50)
    dob = models.DateField()
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)

    
    @property
    def age(self):
        today = date.today()
        db = self.dob
        age = today.year - db.year
        if today.month < db.month or today.month == db.month and today.day < db.day:
            age -= 1
        return age 



class doctor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=True)
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    mobile_no = models.CharField(max_length = 15)
    gender = models.CharField(max_length = 10)
    registration_no = models.CharField(max_length = 20)
    year_of_registration = models.DateField()
    qualification = models.CharField(max_length = 20)
    specialization = models.CharField(max_length = 30)

    





class diseaseinfo(models.Model):

    patient = models.ForeignKey(patient , null=True, on_delete=models.SET_NULL)

    diseasename = models.CharField(max_length = 200)
    no_of_symp = models.IntegerField()
    symptomsname = ArrayField(models.CharField(max_length=200))
    confidence = models.DecimalField(max_digits=5, decimal_places=2)
    consultdoctor = models.CharField(max_length = 200)



class consultation(models.Model):

    patient = models.ForeignKey(patient ,null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(doctor ,null=True, on_delete=models.SET_NULL)
    diseaseinfo = models.OneToOneField(diseaseinfo, null=True, on_delete=models.SET_NULL)
    consultation_date = models.DateField()
    status = models.CharField(max_length = 20)


class Hospital(models.Model):
    hospital_id = models.AutoField
    hospitalname  = models.CharField(max_length=50, default="")
    hospitaladd  = models.CharField(max_length=50, default="")
    hospitalphone  = models.CharField(max_length=50, default="")
    hospitalmap  = models.CharField(max_length=500, default="")
    hospitaltime  = models.DateField(max_length=50, default="")
    hospitalspecial = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.hospitalspecial

class remedies(models.Model):
    remedy_id = models.AutoField
    remedyname  = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="main_app/images", default="")
    remedydesc  = models.CharField(max_length=500, default="")
    


    def __str__(self):
        return self.remedyname

class appointment(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    service = models.CharField(max_length = 50)
    time = models.CharField(max_length = 50)
    note = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.name

