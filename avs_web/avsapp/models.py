from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField
from django.utils import timezone
from multiselectfield import MultiSelectField
import uuid

# Create your models here.

class Staff(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    business_phone = PhoneNumberField()

    def __str__(self):
        return self.user.username
    

class Client(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, unique= True)
    aggrement_plociy = models.BooleanField(default= False)
    aggrement_service = models.BooleanField(default= False)

    ### 1. COMPANY DETAILS
    #1.1 What is your role in the company?
    # CLIENT_ROLE_CHOICE = [
    #     ('1', 'CEO / Director / Senior Manager'),
    #     ('2', 'EHS / Sustainability specialist'),
    #     ('3', 'Marketing specialist'),
    #     ('4', 'Other')
    # ]
    client_role = models.CharField(verbose_name='What is your role in the company?',
        max_length= 100)
    
    #Company Name
    company_name = models.CharField(verbose_name= 'Company Name', max_length=150)

    #5. Company LinkedIn Profile
    linkedin_url = models.URLField(verbose_name='Company LinkedIn Profile', blank=True)

    #6. Business Address
    business_address = models.CharField(verbose_name= 'Business Address', blank= True, max_length= 200)
    location = PlainLocationField(based_fields=['business_address'], zoom=7)

    #7. Business Email *
    business_email = models.EmailField(verbose_name='Business Emai')

    #8. Business Phone Number*
    business_phone = PhoneNumberField(verbose_name = 'Business Phone Number')

    #9. What is the total number of permanent employees in the company? 
    EMPLOYEE_NUM_CHOICE = [
        ('1', '1-9'),
        ('2', '10-49'),
        ('3', '50-249'),
        ('4', '250-349'),
        ('5', '350+')
    ]
    employee_num = models.CharField(verbose_name='What is the total number of permanent employees in the company?',
        max_length= 1, choices= EMPLOYEE_NUM_CHOICE) 

    #10. What category applies to your company's annual turnover?
    ANNUAL_TURNOVER_CHOICE = [
        ('1', 'Below £10.2 million'),
        ('2', 'Between £10.2 million and £36 million'),
        ('3', 'Above £36 million'),
        ('0', 'Prefer not to say')
    ]
    turnover_type = models.CharField(verbose_name="What category applies to your company's annual turnover?",
        max_length= 1, choices= ANNUAL_TURNOVER_CHOICE)

    #11. What industry does the company work in? (choose all appropriate answers)
    industry_type = models.CharField(verbose_name = 'What industry does the company work in?', 
        max_length= 200) 


    def __str__(self):
        return self.user.username

class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, unique= True)
    aggrement_plociy = models.BooleanField(default= False)
    aggrement_service = models.BooleanField(default= False)

    #3. LinkedIn Profile 
    linkedin_url = models.URLField(verbose_name='LinkedIn Profile URL', blank=True)

    #4. Business Name *
    business_name = models.CharField(verbose_name= 'Business Name', max_length= 200)

    #5. Business Address *
    business_address = models.CharField(verbose_name= 'Business Address', blank= True, max_length= 200)
    location = PlainLocationField(based_fields=['business_address'], zoom=7)

    #6. Business Email *
    business_email = models.EmailField(verbose_name='Business Emai')

    #7. Business Phone Number *
    business_phone = PhoneNumberField(verbose_name= 'Business Phone Number')

    #8. What is your role in the company? *
    company_role = models.CharField(verbose_name= 'What is your role in the company?', max_length= 200)

    #9. Your relevant educational qualifications *
    edu_cert = models.TextField(verbose_name= 'Your relevant educational qualifications')

    #10. Membership of professional bodies *
    prof_member = models.TextField(verbose_name= 'Membership of professional bodies')

    #11. How long have you been working in the sustainability consultancy industry? *

    SUS_WORK_EXP_CHOICE = [
        ('1', '0-2 years'),
        ('2', '3-5 years'),
        ('3', '6-10 years'),
        ('4', '11 + years')
    ]
    sus_work_exp = models.CharField(verbose_name= 'How long have you been working in the sustainability consultancy industry?',
        max_length= 1, choices= SUS_WORK_EXP_CHOICE)

    #12. Have you worked for large consultancy companies such as ERM, Arup, Jacobs etc?*
    SUS_PRE_WORK_CHOICE = [
        ('Y', 'Yes'),
        ('N', 'No')
    ]
    sus_pre_work = models.CharField(verbose_name= 'Have you worked for large consultancy companies such as ERM, Arup, Jacobs etc?',
        max_length= 1, choices= SUS_PRE_WORK_CHOICE)

    #If you answered Yes, please specify the name of the consultancy, time frame, your job title, and your role in any projects you were involved with.
    sus_pre_work_details = models.TextField(verbose_name= 'If you answered Yes, please specify the name of the consultancy, time frame, your job title, and your role in any projects you were involved with.',
        blank= True)

    #12. Specialisation (please, describe areas of your expertise in which you offer services) 
    specialisation = models.TextField(verbose_name= 'Specialisation (please, describe areas of your expertise in which you offer services)',
        max_length= 1000)

    #13. Please, provide a brief professional biography including previous employment and projects/work in the field of sustainability. (200 words max)
    prof_biography = models.TextField(verbose_name= 'Please, provide a brief professional biography including previous employment and projects/work in the field of sustainability. (200 words max)',
        max_length= 1000)

    vetted = models.BooleanField(default= False)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.00)

    def __str__(self):
        return self.user.username

class SustainabilityNeedsAssessmentForm(models.Model):
    create_by = models.ForeignKey(Client, on_delete= models.CASCADE)
    create_time = models.DateTimeField(auto_now_add= True)

    #SNAF(sustainability needs assessment form) details, displayed to the client
    ###1.  GENERAL INFORMATION

    #1.1 What is your role in the company?
    # CLIENT_ROLE_CHOICE = [
    #     ('1', 'CEO / Director / Senior Manager'),
    #     ('2', 'EHS / Sustainability specialist'),
    #     ('3', 'Marketing specialist'),
    #     ('4', 'Other')
    # ]
    client_role = models.CharField(verbose_name='1.1. What is your role in the company?',
        max_length= 100)

    #1.2. How long has your company been in business?
    business_duration = models.PositiveIntegerField(verbose_name= '1.2. How long has your company been in business?',
        default= 1)

    #1.3. What is the total number of permanent employees in the company?
    EMPLOYEE_NUM_CHOICE = [
        ('1', '1-9'),
        ('2', '10-49'),
        ('3', '50-249'),
        ('4', '250-349'),
        ('5', '350+')
    ]
    employee_num = models.CharField(verbose_name='1.3. What is the total number of permanent employees in the company?',
        max_length= 1, choices= EMPLOYEE_NUM_CHOICE)
   
    #1.4. Does the company operate:
    OPERATE_TYPE_CHOICE = [
        ('1', 'Locally'),
        ('2', 'Nationally'),
        ('3', 'Internationally')
    ]
    operate_type = models.CharField(verbose_name='1.4. Does the company operate:',
        max_length= 1, choices= OPERATE_TYPE_CHOICE)

    #1.5. What category applies to your company's annual turnover?
    ANNUAL_TURNOVER_CHOICE = [
        ('1', 'Below £10.2 million'),
        ('2', 'Between £10.2 million and £36 million'),
        ('3', 'Above £36 million'),
        ('0', 'Prefer not to say')
    ]
    turnover_type = models.CharField(verbose_name="1.5. What category applies to your company's annual turnover?",
        max_length= 1, choices= ANNUAL_TURNOVER_CHOICE)

    #1.6. Who do you provide your products/services to?
    SERVICE_TYPE_CHOICE = [
        ('1', 'Businesses (B2B)'),
        ('2', 'Consumers (B2C)'),
        ('3', 'Businesses and Consumers (B2B and B2C)')
    ]
    service_type = models.CharField(verbose_name="1.6. Who do you provide your products/services to?",
        max_length= 1, choices= SERVICE_TYPE_CHOICE)

    #1.7. What industry does the company work in? ("choose all appropriate answers")
    # INDUSTRY_FILED_CHOICE = [
    #     ('1', 'Aerospace & Aviation'),
    #     ('2', 'Agriculture & Forestry'),
    #     ('3', 'Automotive'),
    #     ('4', 'Biotechnology'),
    #     ('5', 'Building & Construction'),
    #     ('6', 'Chemicals & Petrochemicals'),
    #     ('7', 'Communications, IT & Technology'),
    #     ('8', 'Education, Research & Training'),
    #     ('9', 'Energy including Renewables'),
    #     ('A', 'Engineering'),
    #     ('B', 'Food & Drink (Retail)'),
    #     ('C', 'Food & Drink (Manufacturing)'),
    #     ('D', 'Other Manufacturing'),
    #     ('E', 'Marine'),
    #     ('F', 'Media & Marketing'),
    #     ('G', 'Medical, Pharmaceutical & Health Services'),
    #     ('H', 'Mining & Quarrying'),
    #     ('I', 'Oil & Gas'),
    #     ('J', 'Real Estate & Property Management'),
    #     ('K', 'Retail (excluding Food & Drink retail)'),
    #     ('L', 'Sport & Leisure'),
    #     ('M', 'Tourism & Hospitality (excluding Food & Drink)'),
    #     ('N', 'Transportation & Highways'),
    #     ('O', 'Other')
    # ]
    industry_type = models.CharField(verbose_name = '1.7. What industry does the company work in? (choose all appropriate answers)',
        max_length= 200)

    ###2. GENERAL  SUSTAINABILITY INFORMATION
   
    #2.1. How do you think integrating sustainability within the company’s processes impacts the company’s performance? (choose all appropriate answers)
    SUS_IMP_TYPE = [
        ('1', 'Creating business opportunities'),
        ('2', 'Presenting a chance to improve company’s competitive advantage'),
        ('3', 'Reducing costs and risks, as well as increasing revenues and intangibles'),
        ('4', 'Promoting revenue growth'),
        ('5', 'Saving costs'),
        ('6', 'Improving reputation and increasing customer loyalty'),
        ('7', 'Helping to build an overall more resilient company'),
        ('8', 'Just a new trend which doesn’t change anything in real life'),
        ('9', 'Costly inconvenience'),
        ('0', 'I don’t know what sustainability practices in business are')
    ]
    sus_impact_field = MultiSelectField(verbose_name= "2.1. How do you think integrating sustainability within the company’s processes impacts the company’s performance? (choose all appropriate answers)",
        choices= SUS_IMP_TYPE)

    #2.2. Does your company already take any sustainability actions?
    # •	Yes (please specify below) ___________________________
    # •	No, but we’re planning on doing so
    # •	No, we don’t have such plans
    sus_actions = models.CharField(verbose_name= '2.2. Does your company already take any sustainability actions?', max_length=100)

    #2.3. If you’re interested in embedding sustainability services in your operations what is your motivation?
    SUS_MTV_CHOICE = [
        ('1', 'Complying with regulatory requirements'),
        ('2', 'Improving competitive advantage'),
        ('3', 'Attracting new and retaining existing customers - both B2B and B2C'),
        ('4', 'Improving companies image'),
        ('5', 'Reducing costs through reducing energy usage, waste, raw material and transport'),
        ('6', 'Fulfilling the growing consumer demand for greener products and services'),
        ('7', 'Attracting funding opportunities and investors'),
        ('8', 'Increasing productivity through increased staff morale, and their motivation'),
        ('9', 'Improving brand image through building positive brand associations'),
        ('A', 'Reducing risk of fines as a business becomes more compliant with legislation'),
        ('B', 'Being in Trend as sustainability is the New Mega Trend now'),
        ('C', 'Making a difference as being sustainable makes a difference. These practices are good for the environment and society.'),
        ('D', 'Increasing profits as all of the above will potentially result in increasing the profit.'),
        ('O', 'Other')
    ]
    sus_motivation = MultiSelectField(verbose_name= "2.3. If you’re interested in embedding sustainability services in your operations what is your motivation? (choose all appropriate answers)",
        choices= SUS_MTV_CHOICE)

    #2.4. If there are any barriers that currently prevent your company from effective management of environmental and social issues, what are they? (choose all appropriate answers):
    BARRIERS_CHOICE = [
        ('1', 'None. We’re managing the issues very effectively'),
        ('2', 'Inappropriate language and unfamiliar concepts & terminology'),
        ('3', 'Lack of finance'),
        ('4', 'Lack of time and other resource'),
        ('5', 'There is no specialist staff at the company who can deal with this'),
        ('6', 'We don’t really know how to engage sustainability in our activities'),
        ('7', 'Short-term business-planning horizon'),
        ('8', 'Lack of appropriate information'),
        ('9', 'Fear of doing things incorrectly'),
        ('O', 'Other reasons')
    ]
    sus_barriers = MultiSelectField(verbose_name= "2.4. If there are any barriers that currently prevent your company from effective management of environmental and social issues, what are they? (choose all appropriate answers)",
        choices= BARRIERS_CHOICE)
    
    #2.5. Do you require assistance to overcome these barriers?
    SUS_ASSISTANCE_CHOICE = [
        ('1', 'Yes, this would help us improve our sustainability performance'),
        ('2', 'No, we can manage without any external help'),
        ('3', 'No, we don’t have any plans to invest into improving the company’s sustainability performance')
    ]
    sus_assistance = models.CharField(verbose_name= '2.5. Do you require assistance to overcome these barriers?',
        max_length= 1, choices= SUS_ASSISTANCE_CHOICE)

    #2.6. How would you find a good consultant If you need one?
    CONSULT_TYPE_CHOICE = [
        ('1', 'Internet. I know exactly what I need and I can find a credible consultant myself. I also have lots of time and good subject knowledge to do a thorough search, to compare available offers and to make sure that the consultant is a good expert in the area. '),
        ('2', 'Professional Service. I’d inquire with a professional agent who has a database of credible consultants available. This will save me time and money as well as allow me to find a consultant with a good reputation and relevant skills.'),
        ('3', 'Personal Recommendation. I’d ask family, friends, or colleagues whether they know of a consultant I can use. I realise that I am taking a risk, as this is a very limited and not independently verifiable way of choosing a consultant for my particular requirements.')
    ]
    sus_consult_type = models.CharField(verbose_name= '2.6. How would you find a good consultant If you need one?',
        max_length= 1, choices= CONSULT_TYPE_CHOICE)

    ### 3. ENVIRONMENT

    #3.1. What proportion of the energy used by the company comes from renewable sources?
    ENERGY_PROPORTION_CHOICE = [
        ('1', 'None'),
        ('2', '1-25%'),
        ('3', '26-50%'),
        ('4', '51-75%'),
        ('5', '76-100%'),
        ('O', 'I don’t know')
    ]
    sus_energy_proportion = models.CharField(verbose_name= '3.1. What proportion of the energy used by the company comes from renewable sources?',
        max_length= 1, choices= ENERGY_PROPORTION_CHOICE)

    #3.2. What proportion of your packaging is made of recycled materials?
    PACKAGING_RECYCLED_PROPORTION_CHOICE = [
        ('1', 'None'),
        ('2', '1-25%'),
        ('3', '26-50%'),
        ('4', '51-75%'),
        ('5', '76-100%'),
        ('O', 'Not applicable because we provide services')        
    ]
    packaging_recycled = models.CharField(verbose_name= '3.2. What proportion of your packaging is made of recycled materials?',
        max_length= 1, choices= PACKAGING_RECYCLED_PROPORTION_CHOICE)

    #3.3. Are your products biodegradable or recyclable?
    PRODUCT_RECYCLABLE_CHOICE = [
        ('1', 'Yes, fully biodegradable or recyclable'),
        ('2', 'Partially biodegradable or recyclable'),
        ('3', 'Neither'),
        ('4', 'Not applicable because we provide services')
    ]
    product_recyclable = models.CharField(verbose_name= '3.3. Are your products biodegradable or recyclable?',
        max_length= 1, choices= PRODUCT_RECYCLABLE_CHOICE)

    #3.4. How often do you measure your environmental performance in the organisation?
    MEASURE_FREQ_CHOICE = [
        ('1', 'Monthly'),
        ('2', 'Every 6 months'),
        ('3', 'Annually'),
        ('4', 'Every 3 to 5 years'),
        ('5', 'Never')
    ]
    env_measure_freq = models.CharField(verbose_name= '3.4. How often do you measure your environmental performance in the organisation?',
        max_length= 1, choices= MEASURE_FREQ_CHOICE)

    #3.5. How many times in the last 5 years has the company entered a competition for the best environmental practices and initiatives?
    ENV_COMP_FREQ_CHOICE = [
        ('0', 'None'),
        ('1', 'Once'),
        ('2', 'Twice'),
        ('3', 'Three times'),
        ('4', 'Four times'),
        ('5', 'Five times')
    ]
    env_comp_freq = models.CharField(verbose_name= '3.5. How many times in the last 5 years has the company entered a competition for the best environmental practices and initiatives?', 
        max_length= 1, choices= ENV_COMP_FREQ_CHOICE)

    ### 4. SOCIAL

    #4.1. How many times in the last 5 years has your company invested (financially or through volunteering) in local community projects?
    LOCAL_INVEST_FREQ_CHOICE = [
        ('0', 'Never'),
        ('1', '1 - 2 times'),
        ('2', '3 - 5 times'),
        ('3', 'More than 5 times')
    ]
    local_invest_freq = models.CharField(verbose_name= '4.1. How many times in the last 5 years has your company invested (financially or through volunteering) in local community projects?',
        max_length= 1, choices= LOCAL_INVEST_FREQ_CHOICE)

    #4.2.What proportion of your contracts involve local suppliers?
    LOCAL_SUP_PROPORTION_CHOICE = [
        ('0', '0%'),
        ('1', '1 - 25%'),
        ('2', '26 - 50%'),
        ('3', '51 - 75%'),
        ('4', '76 - 100%'),
        ('N', 'Not applicable because we provide services')
    ]
    local_sup_proportion = models.CharField(verbose_name= '4.2.What proportion of your contracts involve local suppliers?',
        max_length= 1, choices= LOCAL_SUP_PROPORTION_CHOICE)

    #4.3. What proportion of your company's management are women?
    FEMALE_EMPLOYEE_PROPORTION_CHOICE = [
        ('0', '0%'),
        ('1', '1 - 25%'),
        ('2', '26 - 50%'),
        ('3', '51 - 75%'),
        ('4', '76 - 100%')
    ]
    female_employee_proportion = models.CharField(verbose_name= "4.3. What proportion of your company's management are women?",
        max_length= 1, choices= FEMALE_EMPLOYEE_PROPORTION_CHOICE)

    #4.4. What proportion of your company's workforce are registered disabled?
    DISABLE_EMPLOYEE_PROPORTION_CHOICE = [
        ('0', '0%'),
        ('1', '1 - 25%'),
        ('2', '26 - 50%'),
        ('3', '51 - 75%'),
        ('4', '76 - 100%')
    ]
    disable_employee_proportion = models.CharField(verbose_name= "4.4. What proportion of your company's workforce are registered disabled?",
        max_length= 1, choices= DISABLE_EMPLOYEE_PROPORTION_CHOICE)

    #4.5. How many times in the last 5 years has the company entered a competition on best social practices and initiatives?
    SOCIAL_COMP_FREQ_CHOICE = [
        ('0', 'None'),
        ('1', 'Once'),
        ('2', 'Twice'),
        ('3', 'Three times'),
        ('4', 'Four times'),
        ('5', 'Five times')
    ]
    social_comp_freq = models.CharField(verbose_name= '4.5. How many times in the last 5 years has the company entered a competition on best social practices and initiatives?',
        max_length= 1, choices= SOCIAL_COMP_FREQ_CHOICE)

    ### 5. GOVERNANCE AND STRATEGY

    #5.1. Does the company regularly monitor changes in legislation and regulations related to sustainability aspects in business? 
    REGULATION_MONITOR_FREQ_CHOICES = [
        ('1', 'Yes, monthly'),
        ('2', 'Yes, every 6 months'),
        ('3', 'Yes, yearly'),
        ('0', 'No'),
        ('N', 'I don’t know')
    ]
    sus_regualtion_monitor_freq = models.CharField(verbose_name= '5.1. Does the company regularly monitor changes in legislation and regulations related to sustainability aspects in business?',
        max_length= 1, choices= REGULATION_MONITOR_FREQ_CHOICES)

    #5.2. Is the sustainability agenda included in the company’s strategy?
    SUS_AGENDA_CHOICE = [
        ('1', 'Yes'),
        ('0', 'No'),
        ('N', 'I don’t know')
    ]
    sus_agenda = models.CharField(verbose_name= '5.2. Is the sustainability agenda included in the company’s strategy?',
        max_length= 1, choices= SUS_AGENDA_CHOICE)

    #5.3. Does the company produce an annual sustainability report?
    SUS_ANNUAL_REPORT_CHOICE = [
        ('1', 'Yes'),
        ('0', 'No'),
        ('N', 'I don’t know')
    ]
    sus_annual_report = models.CharField(verbose_name= '5.3. Does the company produce an annual sustainability report?',
        max_length= 1, choices= SUS_ANNUAL_REPORT_CHOICE)

    #5.4. If the company doesn’t produce an annual sustainability report, is a sustainability section included in the company’s annual report?
    SUS_IN_ANNUAL_REPORT_CHOICE = [
        ('1', 'Yes'),
        ('0', 'No'),
        ('N', 'I don’t know'),
        ('2', 'The company doesn’t produce an annual report.')        
    ]
    sus_in_annual_report = models.CharField(verbose_name= '5.4. If the company doesn’t produce an annual sustainability report, is a sustainability section included in the company’s annual report?', 
        max_length= 1, choices= SUS_IN_ANNUAL_REPORT_CHOICE)

    #5.5. Does the company set sustainability targets to be achieved each year?
    SUS_PLAN_TARGET_CHOICE = [
        ('1', 'Yes'),
        ('0', 'No'),
        ('N', 'I don’t know')
    ]
    sus_plan_target = models.CharField(verbose_name= '5.5. Does the company set sustainability targets to be achieved each year?',
        max_length= 1, choices= SUS_PLAN_TARGET_CHOICE)

    #5.6. How many times in the last 5 years has the company entered a competition on best sustainability or ESG practices and initiatives?
    SUS_COMP_FREQ_CHOICE = [
        ('0', 'None'),
        ('1', 'Once'),
        ('2', 'Twice'),
        ('3', 'Three times'),
        ('4', 'Four times'),
        ('5', 'Five times')        
    ]
    sus_comp_freq = models.CharField(verbose_name= '5.6. How many times in the last 5 years has the company entered a competition on best sustainability or ESG practices and initiatives?',
        max_length= 1, choices= SUS_COMP_FREQ_CHOICE)
    

class ClientServiceEnquiryForm(models.Model):
    create_by = models.ForeignKey(Client, on_delete= models.CASCADE)
    create_time = models.DateTimeField(auto_now_add= True)

    ###II. PROJECT DETAILS

    #1. What are your objectives for the project?* 
    proj_obj = models.TextField(verbose_name= 'What are your objectives for the project?')

    #2. What area of sustainability are you looking for services in?
    proj_area = models.CharField(verbose_name= 'What area of sustainability are you looking for services in?',
        max_length= 200)

    #3. Identify specific services you are looking for 
    proj_spec_service = models.CharField(verbose_name= 'Identify specific services you are looking for',
        max_length= 200)

    #4. Please specify project dates (even if approximately)*
    proj_start_date = models.DateField(verbose_name= 'Start date', 
        help_text= 'Please specify project dates (even if approximately)',
        null=True)
    proj_end_date = models.DateField(verbose_name= 'End date',
        help_text= 'Please specify project dates (even if approximately)',
        null=True)

    #5. Are the start and end dates flexible?*
    PROJ_FLEX_CHOICE = [
        ('1', 'Yes, quite flexible'),
        ('2', 'Some flexibility'),
        ('0', 'No, not flexible at all')
    ]
    proj_flex = models.CharField(verbose_name= 'Are the start and end dates flexible?',
        max_length= 1, choices= PROJ_FLEX_CHOICE)

    #Describe in detail what kind of work you need to be done. Please be as specific as possible, so that we can find the best suitable consultant for you.
    proj_details = models.TextField(verbose_name= 'Describe in detail what kind of work you need to be done. Please be as specific as possible, so that we can find the best suitable consultant for you.',
        max_length= 1000)

    ###III. CONSULTANT DETAILS

    #1. Please specify where the consultant should be located
    consult_location = models.CharField(verbose_name= 'Please specify where the consultant should be located',
        max_length= 200, help_text= '')

    #2. Would you agree to work with a graduate consultant if senior consultants aren’t available for your project or specific dates?
    ALLOW_GRAD_CONSULT_CHOICE = [
        ('1', 'Yes'),
        ('2', 'No')
    ]
    allow_grad_consult = models.CharField(verbose_name= 'Would you agree to work with a graduate consultant if senior consultants aren’t available for your project or specific dates? ', 
        max_length= 1, choices= ALLOW_GRAD_CONSULT_CHOICE)

    ###Please prioritise consultant characteristics so that we can find the best suitable consultant for you. Rate the following characteristics according to your priorities on a scale of 1-5 where 1-extremely important and 5 - least important.
    PRIORITY_CHOICES = [
        (1, '1-Extremely Important'),
        (2, '2-Fairly important'),
        (3, '3-Important'),
        (4, '4-Slightly Important'),
        (5, '5-Least important')
    ]

    #Consultant experience
    priority_consult_exp = models.CharField(verbose_name= 'Consultant experience', max_length= 1, choices= PRIORITY_CHOICES)

    #Consultant location
    priority_consult_loc = models.CharField(verbose_name= 'Consultant location', max_length= 1, choices= PRIORITY_CHOICES)

    #Cost of the work
    priority_consult_cost = models.CharField(verbose_name= 'Cost of the work', max_length= 1, choices= PRIORITY_CHOICES)

    #Dates of the project
    priority_project_date = models.CharField(verbose_name= 'Dates of the project', max_length= 1, choices= PRIORITY_CHOICES)

    #Consultant Satisfaction Rating/feedback from previous clients
    priority_consult_rating = models.CharField(verbose_name= 'Consultant Satisfaction Rating/feedback from previous clients',
        max_length= 1, choices= PRIORITY_CHOICES)

    def __str__(self):
        return f'ecsf {self.id} from {self.create_by.user.username}'

class ServiceInvitation(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4(), editable=False)

    invitation_event = models.ForeignKey(ClientServiceEnquiryForm, on_delete= models.CASCADE, null= True)

    invitaiton_to = models.ForeignKey(Consultant, on_delete= models.CASCADE)

    create_time = models.DateTimeField(auto_now_add= True)

    INVITATION_STATUS_CHOICE = [
        ('0', 'None'),
        ('1', 'Accept'),
        ('2', 'Waiting'),
        ('3', 'Backup'),
        ('4', 'Refuse')
    ]
    invitation_status = models.CharField(verbose_name= 'Consultant Invitation Status',
        max_length= 1, choices= INVITATION_STATUS_CHOICE, default= '0')

    PAYMENT_STATUS_CHOICE = [
        ('0', 'Waiting'),
        ('1', 'Accept'),
        ('2', 'Refuse'),
        ('3', 'Payed')
    ]
    payment_status = models.CharField(verbose_name= 'Client Payment Status',
        max_length= 1, choices= PAYMENT_STATUS_CHOICE, default= '0')

    update_time = models.DateTimeField(auto_now= True)

    #if accept the invitaiton, then the consultant would give a bid price for the service
    bid_price = models.IntegerField(verbose_name= 'Bid Price(£):', null= True, blank= True)

    def __str__(self):
        return f'{self.invitation_event}'
