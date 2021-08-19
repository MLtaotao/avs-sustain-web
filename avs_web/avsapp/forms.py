from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from location_field.forms.plain import PlainLocationField

from .models import Staff, Client, Consultant


class LoginForm(forms.Form):
    username = forms.CharField(widget= forms.TextInput(
        attrs={"type":"username", "class":"form-control", "id":"floatingInput"}))
    password = forms.CharField(widget= forms.PasswordInput(
        attrs={"type":"password", "class":"form-control", "id":"floatingPassword"}))

# form for register new user
class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# user edit form
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

#Staff register form
class StaffForm(forms.ModelForm):
    business_phone = PhoneNumberField()
    class Meta:
        model = Staff
        fields = ['business_phone']

#Client register form
class ClientForm(forms.ModelForm):
    
    class Meta:
        model = Client
        fields = ['aggrement_plociy', 'aggrement_service']
        
#Client edit form
class ClientEditForm(forms.ModelForm):
    business_phone = PhoneNumberField()
    city = forms.CharField()
    location = PlainLocationField(based_fields=['city'],
                                  initial='53.801277, -1.548567')
    class Meta:
        model = Client
        fields = ['business_phone', 'company_name', 'city', 'location']

#Consulutant register form
class ConsultantForm(forms.ModelForm):
    
    class Meta:
        model = Consultant
        fields = ['aggrement_plociy', 'aggrement_service']

#Consultant edit form
class ConsultantEditForm(forms.ModelForm):
    business_phone = PhoneNumberField()
    city = forms.CharField()
    location = PlainLocationField(based_fields=['city'],
                                  initial='53.801277, -1.548567')
    class Meta:
        model = Consultant
        fields = ['business_phone', 'description', 'city', 'location']
    

    

