from django import forms
import floppyforms
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from location_field.forms.plain import PlainLocationField

from .models import Staff, Client, Consultant, SustainabilityNeedsAssessmentForm, ClientServiceEnquiryForm, ServiceInvitation


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

# #user profile form
# class UserViewForm(forms.ModelForm):

#     class Meta:
#         model = User
#         fields = ['username', 'email']

# user edit form
class UserEditForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={'readonly':True}),
            'email': forms.EmailInput(attrs={'readonly':True}),
        }

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
    business_address = forms.CharField()
    location = PlainLocationField(based_fields=['business_address'])

    class Meta:
        CLIENT_ROLE_CHOICE = [
            'CEO / Director / Senior Manager',
            'EHS / Sustainability specialist',
            'Marketing specialist',
            'Your answer __________________________'
        ]
        INDUSTRY_FILED_CHOICE = [
            'Aerospace & Aviation',
            'Agriculture & Forestry',
            'Automotive',
            'Biotechnology',
            'Building & Construction',
            'Chemicals & Petrochemicals',
            'Communications, IT & Technology',
            'Education, Research & Training',
            'Energy including Renewables',
            'Engineering',
            'Food & Drink (Retail)',
            'Food & Drink (Manufacturing)',
            'Other Manufacturing',
            'Marine',
            'Media & Marketing',
            'Medical, Pharmaceutical & Health Services',
            'Mining & Quarrying',
            'Oil & Gas',
            'Real Estate & Property Management',
            'Retail (excluding Food & Drink retail)',
            'Sport & Leisure',
            'Tourism & Hospitality (excluding Food & Drink)',
            'Transportation & Highways',
            'Other (please, specify) ________'
        ]
        model = Client
        fields = ['client_role', 'company_name', 'linkedin_url', 'business_address', 'location',
                'business_email', 'business_phone', 'employee_num', 'turnover_type', 'industry_type']
        widgets = {
            'client_role': floppyforms.widgets.Input(datalist= CLIENT_ROLE_CHOICE),
            'industry_type': floppyforms.widgets.Input(datalist= INDUSTRY_FILED_CHOICE),
        }

#Consulutant register form
class ConsultantForm(forms.ModelForm):
    
    class Meta:
        model = Consultant
        fields = ['aggrement_plociy', 'aggrement_service']

#Consultant edit form
class ConsultantEditForm(forms.ModelForm):
    business_phone = PhoneNumberField()
    business_address = forms.CharField()
    location = PlainLocationField(based_fields=['business_address'])

    class Meta:
        model = Consultant
        fields = ['linkedin_url', 'business_name', 'business_address', 'location',
            'business_email', 'business_phone', 'company_role', 'edu_cert',
            'prof_member', 'sus_work_exp', 'sus_pre_work', 'sus_pre_work_details',
            'specialisation', 'prof_biography']
        widgets = {
            'sus_pre_work_details': forms.Textarea(attrs={'rows':5}),
            'specialisation': forms.Textarea(attrs={'rows':5}),
            'prof_biography': forms.Textarea(attrs={'rows':5}),            
        }

#Sustainability Needs Assessment Form(SNAF) 1-5

#SNAF1
class SNAF1(forms.ModelForm):

    class Meta:
        CLIENT_ROLE_CHOICE = [
            'CEO / Director / Senior Manager',
            'EHS / Sustainability specialist',
            'Marketing specialist',
            'Your answer __________________________'
        ]
        INDUSTRY_FILED_CHOICE = [
            'Aerospace & Aviation',
            'Agriculture & Forestry',
            'Automotive',
            'Biotechnology',
            'Building & Construction',
            'Chemicals & Petrochemicals',
            'Communications, IT & Technology',
            'Education, Research & Training',
            'Energy including Renewables',
            'Engineering',
            'Food & Drink (Retail)',
            'Food & Drink (Manufacturing)',
            'Other Manufacturing',
            'Marine',
            'Media & Marketing',
            'Medical, Pharmaceutical & Health Services',
            'Mining & Quarrying',
            'Oil & Gas',
            'Real Estate & Property Management',
            'Retail (excluding Food & Drink retail)',
            'Sport & Leisure',
            'Tourism & Hospitality (excluding Food & Drink)',
            'Transportation & Highways',
            'Other (please, specify) ________'
        ]

        model = SustainabilityNeedsAssessmentForm
        fields = [
            'client_role', 'business_duration', 'employee_num', 'operate_type', 
            'turnover_type', 'service_type', 'industry_type'
        ]
        widgets = {
            'client_role': floppyforms.widgets.Input(datalist= CLIENT_ROLE_CHOICE),
            'industry_type': floppyforms.widgets.Input(datalist= INDUSTRY_FILED_CHOICE),
        }

###2. GENERAL  SUSTAINABILITY INFORMATION
class SNAF2(forms.ModelForm):

    class Meta:
        SUS_ACTION_CHOICE = [
            'Yes (please specify) _____________',
            'No, but we’re planning on doing so',
            'No, we don’t have such plans'
        ]

        model = SustainabilityNeedsAssessmentForm
        fields = [
            'sus_impact_field', 'sus_actions', 'sus_motivation', 'sus_barriers',
            'sus_assistance', 'sus_consult_type'
        ]
        widgets = {
            'sus_actions': floppyforms.widgets.Input(datalist= SUS_ACTION_CHOICE)
        }        

### 3. ENVIRONMENT    
class SNAF3(forms.ModelForm):
    class Meta:
        model = SustainabilityNeedsAssessmentForm
        fields = [
            'sus_energy_proportion', 'packaging_recycled', 'product_recyclable',
            'env_measure_freq', 'env_comp_freq'
        ]

### 4. SOCIAL
class SNAF4(forms.ModelForm):
    class Meta:
        model = SustainabilityNeedsAssessmentForm
        fields = [
            'local_invest_freq', 'local_sup_proportion', 'female_employee_proportion',
            'disable_employee_proportion', 'social_comp_freq'
        ]

### 5. GOVERNANCE AND STRATEGY
class SNAF5(forms.ModelForm):
    class Meta:
        model = SustainabilityNeedsAssessmentForm
        fields = [
            'sus_regualtion_monitor_freq', 'sus_agenda', 'sus_annual_report',
            'sus_in_annual_report', 'sus_plan_target', 'sus_comp_freq'
        ]
     

### Enquiry for Consultancy Services

#I. COMPANY DETAILS models client
class ECSF1(forms.ModelForm):
    business_address = forms.CharField()
    location = PlainLocationField(based_fields=['business_address'])

    class Meta:
        CLIENT_ROLE_CHOICE = [
            'CEO / Director / Senior Manager',
            'EHS / Sustainability specialist',
            'Marketing specialist',
            'Your answer __________________________'
        ]
        INDUSTRY_FILED_CHOICE = [
            'Aerospace & Aviation',
            'Agriculture & Forestry',
            'Automotive',
            'Biotechnology',
            'Building & Construction',
            'Chemicals & Petrochemicals',
            'Communications, IT & Technology',
            'Education, Research & Training',
            'Energy including Renewables',
            'Engineering',
            'Food & Drink (Retail)',
            'Food & Drink (Manufacturing)',
            'Other Manufacturing',
            'Marine',
            'Media & Marketing',
            'Medical, Pharmaceutical & Health Services',
            'Mining & Quarrying',
            'Oil & Gas',
            'Real Estate & Property Management',
            'Retail (excluding Food & Drink retail)',
            'Sport & Leisure',
            'Tourism & Hospitality (excluding Food & Drink)',
            'Transportation & Highways',
            'Other (please, specify) ________'
        ]
        model = Client
        fields = ['client_role', 'company_name', 'linkedin_url', 'business_address', 'location',
                'business_email', 'business_phone', 'employee_num', 'turnover_type', 'industry_type']
        widgets = {
            'client_role': floppyforms.widgets.Input(datalist= CLIENT_ROLE_CHOICE),
            'industry_type': floppyforms.widgets.Input(datalist= INDUSTRY_FILED_CHOICE),
        }

#II. PROJECT DETAILS
class DateInput(forms.DateInput):
    input_type = 'date'

class ECSF2(forms.ModelForm):
    proj_start_date = forms.DateField(widget= DateInput)
    proj_end_date = forms.DateField(widget= DateInput)

    class Meta:
        SUS_SERVICE_CHOICE = [
            'Environmental (e.g. waste, EMS, water usage, Environmental Impact Assessment etc)',
            'Energy and Carbon Footprint (e.g. energy use reduction, energy audit, carbon offsets etc)',
            'Social (e.g. social value calculation, modern anti-slavery policy, community engagement opportunities etc)',
            'Governance and Strategy (e.g. embedding sustainability in company’s strategy, sustainability reporting etc)',
            'Other areas (please specify)',
            'I’m not sure (Please, take our free Sustainability Needs Assessment to understand what you need to focus on)'
        ]
        model = ClientServiceEnquiryForm
        fields = ['proj_obj', 'proj_area', 'proj_spec_service', 'proj_start_date', 'proj_end_date',
                'proj_flex', 'proj_details']
        widgets = {
            'proj_area': floppyforms.widgets.Input(datalist= SUS_SERVICE_CHOICE),
        }

#III. CONSULTANT DETAILS
class ECSF3(forms.ModelForm):
    class Meta:
        CONSULTANT_LOCATION_CHOICE = [
            'United Kingdom',
            'Western and Eastern Europe)',
            'North America (USA and Canada)',
            'Central and South America',
            'Asia',
            'Africa',
            'Australia and Oceania',
            'Specific location (please specify)',
            'Location isn’t important'
        ]
        model = ClientServiceEnquiryForm
        fields = ['consult_location', 'allow_grad_consult', 'priority_consult_exp', 'priority_consult_loc',
                'priority_consult_cost', 'priority_project_date', 'priority_consult_rating']
        widgets = {
            'consult_location': floppyforms.widgets.Input(datalist= CONSULTANT_LOCATION_CHOICE),
        }

class Consultant_ECSF(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(Consultant_ECSF, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True

    class Meta:
        model = ClientServiceEnquiryForm
        fields = ['proj_obj', 'proj_area', 'proj_spec_service', 'proj_start_date', 'proj_end_date',
                'proj_flex', 'proj_details','consult_location', 'allow_grad_consult', 'priority_consult_exp',
                'priority_consult_loc','priority_consult_cost', 'priority_project_date', 'priority_consult_rating']

class InvitationBidForm(forms.ModelForm):
    bid_price = forms.IntegerField(required= False)
    class Meta:
        model = ServiceInvitation
        fields = ['bid_price']

class CilentViewConsultantForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CilentViewConsultantForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True

    class Meta:
        model = Consultant
        fields = ['company_role', 'edu_cert', 'prof_member', 'sus_work_exp', 
            'sus_pre_work', 'sus_pre_work_details', 'specialisation', 'prof_biography',
            'rating', 'vetted']

class InvitationPaymentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(InvitationPaymentForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
    class Meta:
        model = ServiceInvitation
        fields = ['bid_price']

# class SNAF_Check_Form(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(SNAF_Check_Form, self).__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['disabled'] = True

#     class Meta:
#         model = SustainabilityNeedsAssessmentForm
#         fields = []