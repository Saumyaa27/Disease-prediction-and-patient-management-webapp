from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)

    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="Patient")
    Name = models.CharField(max_length=80,default = None,null=True)
    Age = models.IntegerField(default = None,null=True)
    Address = models.TextField(max_length=300,null=True)
    Gender = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.Name


class Specialization(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True,default = None)

    def __str__(self):
        return self.Name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="Doctor")
    Name = models.CharField(max_length=80,default = None,null=True)
    Age = models.IntegerField(default = None,null=True)
    Address = models.TextField(max_length=300,null=True)
    Gender = models.CharField(max_length=30,null=True)
    Specialization = models.ForeignKey(Specialization,on_delete=models.PROTECT,related_name="Doctors")
    contact  = models.IntegerField(null=True)
    Qualification = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.Name


from django.db import models

class Reports(models.Model):
    name= models.CharField(max_length=100)
    Description = models.CharField(max_length=500)
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="Reports")
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")
    Doctors = models.ManyToManyField(Doctor,related_name="Reports",null=True,blank=True)
    
    def __str__(self):
        return self.name + ": " + str(self.filepath)

class Disease(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True,default = None)
    Specialization = models.ForeignKey(Specialization,on_delete=models.CASCADE,related_name="Diseases")

    def __str__(self):
        return self.Name

class Treatment(models.Model):
    Patient = models.ForeignKey(Patient,on_delete=models.CASCADE,related_name="Treatments")
    Doctor = models.ForeignKey(Doctor,related_name="Treatments",null=True,on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    Disease = models.ForeignKey(Disease,on_delete=models.PROTECT,related_name="Patients")
    Prescription = models.TextField(max_length=800,null=True,default = None,blank=True)
    Appointment = models.DateField(null=True,default = None,blank=True)

