from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    business_phone = PhoneNumberField()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    business_phone = PhoneNumberField()
    company_name = models.CharField(max_length=150, blank= True)
    city = models.CharField(max_length=255, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True)

class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    business_phone = PhoneNumberField()
    description = models.TextField(max_length=400, blank= True)
    city = models.CharField(max_length=255, blank=True)
    location = PlainLocationField(based_fields=['city'], zoom=7, blank=True)
    vetted = models.BooleanField(default= False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, blank=True)

