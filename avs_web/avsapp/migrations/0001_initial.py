# Generated by Django 3.2.5 on 2021-09-14 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import multiselectfield.db.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggrement_plociy', models.BooleanField(default=False)),
                ('aggrement_service', models.BooleanField(default=False)),
                ('client_role', models.CharField(max_length=100, verbose_name='What is your role in the company?')),
                ('company_name', models.CharField(max_length=150, verbose_name='Company Name')),
                ('linkedin_url', models.URLField(blank=True, verbose_name='Company LinkedIn Profile')),
                ('business_address', models.CharField(blank=True, max_length=200, verbose_name='Business Address')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('business_email', models.EmailField(max_length=254, verbose_name='Business Emai')),
                ('business_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Business Phone Number')),
                ('employee_num', models.CharField(choices=[('1', '1-9'), ('2', '10-49'), ('3', '50-249'), ('4', '250-349'), ('5', '350+')], max_length=1, verbose_name='What is the total number of permanent employees in the company?')),
                ('turnover_type', models.CharField(choices=[('1', 'Below £10.2 million'), ('2', 'Between £10.2 million and £36 million'), ('3', 'Above £36 million'), ('0', 'Prefer not to say')], max_length=1, verbose_name="What category applies to your company's annual turnover?")),
                ('industry_type', models.CharField(max_length=200, verbose_name='What industry does the company work in?')),
                ('proj_obj', models.TextField(verbose_name='What are your objectives for the project?')),
                ('proj_area', models.CharField(max_length=200, verbose_name='What area of sustainability are you looking for services in?')),
                ('proj_spec_service', models.CharField(max_length=200, verbose_name='Identify specific services you are looking for')),
                ('proj_start_date', models.DateField(help_text='Please specify project dates (even if approximately)', verbose_name='Start date')),
                ('proj_end_date', models.DateField(help_text='Please specify project dates (even if approximately)', verbose_name='End date')),
                ('proj_flex', models.CharField(choices=[('1', 'Yes, quite flexible'), ('2', 'Some flexibility'), ('0', 'No, not flexible at all')], max_length=1, verbose_name='Are the start and end dates flexible?')),
                ('proj_details', models.TextField(max_length=1000, verbose_name='Describe in detail what kind of work you need to be done. Please be as specific as possible, so that we can find the best suitable consultant for you.')),
                ('consult_location', models.CharField(max_length=200, verbose_name='Please specify where the consultant should be located')),
                ('allow_grad_consult', models.CharField(choices=[('1', 'Yes'), ('2', 'No')], max_length=1, verbose_name='Would you agree to work with a graduate consultant if senior consultants aren’t available for your project or specific dates? ')),
                ('priority_consult_exp', models.CharField(choices=[('1', '1-Extremely Important'), ('2', '2-Fairly important'), ('3', '3-Important'), ('4', '4-Slightly Important'), ('5', '5-Least important')], max_length=1, verbose_name='Consultant experience')),
                ('priority_consult_loc', models.CharField(choices=[('1', '1-Extremely Important'), ('2', '2-Fairly important'), ('3', '3-Important'), ('4', '4-Slightly Important'), ('5', '5-Least important')], max_length=1, verbose_name='Consultant location')),
                ('priority_consult_cost', models.CharField(choices=[('1', '1-Extremely Important'), ('2', '2-Fairly important'), ('3', '3-Important'), ('4', '4-Slightly Important'), ('5', '5-Least important')], max_length=1, verbose_name='Cost of the work')),
                ('priority_project_date', models.CharField(choices=[('1', '1-Extremely Important'), ('2', '2-Fairly important'), ('3', '3-Important'), ('4', '4-Slightly Important'), ('5', '5-Least important')], max_length=1, verbose_name='Dates of the project')),
                ('priority_consult_rating', models.CharField(choices=[('1', '1-Extremely Important'), ('2', '2-Fairly important'), ('3', '3-Important'), ('4', '4-Slightly Important'), ('5', '5-Least important')], max_length=1, verbose_name='Consultant Satisfaction Rating/feedback from previous clients')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SustainabilityNeedsAssessmentForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('client_role', models.CharField(max_length=100, verbose_name='1.1. What is your role in the company?')),
                ('business_duration', models.PositiveIntegerField(default=1, verbose_name='1.2. How long has your company been in business?')),
                ('employee_num', models.CharField(choices=[('1', '1-9'), ('2', '10-49'), ('3', '50-249'), ('4', '250-349'), ('5', '350+')], max_length=1, verbose_name='1.3. What is the total number of permanent employees in the company?')),
                ('operate_type', models.CharField(choices=[('1', 'Locally'), ('2', 'Nationally'), ('3', 'Internationally')], max_length=1, verbose_name='1.4. Does the company operate:')),
                ('turnover_type', models.CharField(choices=[('1', 'Below £10.2 million'), ('2', 'Between £10.2 million and £36 million'), ('3', 'Above £36 million'), ('0', 'Prefer not to say')], max_length=1, verbose_name="1.5. What category applies to your company's annual turnover?")),
                ('service_type', models.CharField(choices=[('1', 'Businesses (B2B)'), ('2', 'Consumers (B2C)'), ('3', 'Businesses and Consumers (B2B and B2C)')], max_length=1, verbose_name='1.6. Who do you provide your products/services to?')),
                ('industry_type', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Aerospace & Aviation'), ('2', 'Agriculture & Forestry'), ('3', 'Automotive'), ('4', 'Biotechnology'), ('5', 'Building & Construction'), ('6', 'Chemicals & Petrochemicals'), ('7', 'Communications, IT & Technology'), ('8', 'Education, Research & Training'), ('9', 'Energy including Renewables'), ('A', 'Engineering'), ('B', 'Food & Drink (Retail)'), ('C', 'Food & Drink (Manufacturing)'), ('D', 'Other Manufacturing'), ('E', 'Marine'), ('F', 'Media & Marketing'), ('G', 'Medical, Pharmaceutical & Health Services'), ('H', 'Mining & Quarrying'), ('I', 'Oil & Gas'), ('J', 'Real Estate & Property Management'), ('K', 'Retail (excluding Food & Drink retail)'), ('L', 'Sport & Leisure'), ('M', 'Tourism & Hospitality (excluding Food & Drink)'), ('N', 'Transportation & Highways'), ('O', 'Other')], max_length=47, verbose_name='1.7. What industry does the company work in? (choose all appropriate answers)')),
                ('sus_impact_field', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Creating business opportunities'), ('2', 'Presenting a chance to improve company’s competitive advantage'), ('3', 'Reducing costs and risks, as well as increasing revenues and intangibles'), ('4', 'Promoting revenue growth'), ('5', 'Saving costs'), ('6', 'Improving reputation and increasing customer loyalty'), ('7', 'Helping to build an overall more resilient company'), ('8', 'Just a new trend which doesn’t change anything in real life'), ('9', 'Costly inconvenience'), ('0', 'I don’t know what sustainability practices in business are')], max_length=19, verbose_name='2.1. How do you think integrating sustainability within the company’s processes impacts the company’s performance? (choose all appropriate answers)')),
                ('sus_actions', models.CharField(max_length=100, verbose_name='2.2. Does your company already take any sustainability actions?')),
                ('sus_motivation', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'Complying with regulatory requirements'), ('2', 'Improving competitive advantage'), ('3', 'Attracting new and retaining existing customers - both B2B and B2C'), ('4', 'Improving companies image'), ('5', 'Reducing costs through reducing energy usage, waste, raw material and transport'), ('6', 'Fulfilling the growing consumer demand for greener products and services'), ('7', 'Attracting funding opportunities and investors'), ('8', 'Increasing productivity through increased staff morale, and their motivation'), ('9', 'Improving brand image through building positive brand associations'), ('A', 'Reducing risk of fines as a business becomes more compliant with legislation'), ('B', 'Being in Trend as sustainability is the New Mega Trend now'), ('C', 'Making a difference as being sustainable makes a difference. These practices are good for the environment and society.'), ('D', 'Increasing profits as all of the above will potentially result in increasing the profit.'), ('O', 'Other')], max_length=27, verbose_name='2.3. If you’re interested in embedding sustainability services in your operations what is your motivation? (choose all appropriate answers)')),
                ('sus_barriers', multiselectfield.db.fields.MultiSelectField(choices=[('1', 'None. We’re managing the issues very effectively'), ('2', 'Inappropriate language and unfamiliar concepts & terminology'), ('3', 'Lack of finance'), ('4', 'Lack of time and other resource'), ('5', 'There is no specialist staff at the company who can deal with this'), ('6', 'We don’t really know how to engage sustainability in our activities'), ('7', 'Short-term business-planning horizon'), ('8', 'Lack of appropriate information'), ('9', 'Fear of doing things incorrectly'), ('O', 'Other reasons')], max_length=19, verbose_name='2.4. If there are any barriers that currently prevent your company from effective management of environmental and social issues, what are they? (choose all appropriate answers)')),
                ('sus_assistance', models.CharField(choices=[('1', 'Yes, this would help us improve our sustainability performance'), ('2', 'No, we can manage without any external help'), ('3', 'No, we don’t have any plans to invest into improving the company’s sustainability performance')], max_length=1, verbose_name='2.5. Do you require assistance to overcome these barriers?')),
                ('sus_consult_type', models.CharField(choices=[('1', 'Internet. I know exactly what I need and I can find a credible consultant myself. I also have lots of time and good subject knowledge to do a thorough search, to compare available offers and to make sure that the consultant is a good expert in the area. '), ('2', 'Professional Service. I’d inquire with a professional agent who has a database of credible consultants available. This will save me time and money as well as allow me to find a consultant with a good reputation and relevant skills.'), ('3', 'Personal Recommendation. I’d ask family, friends, or colleagues whether they know of a consultant I can use. I realise that I am taking a risk, as this is a very limited and not independently verifiable way of choosing a consultant for my particular requirements.')], max_length=1, verbose_name='2.6. How would you find a good consultant If you need one?')),
                ('sus_energy_proportion', models.CharField(choices=[('1', 'None'), ('2', '1-25%'), ('3', '26-50%'), ('4', '51-75%'), ('5', '76-100%'), ('O', 'I don’t know')], max_length=1, verbose_name='3.1. What proportion of the energy used by the company comes from renewable sources?')),
                ('packaging_recycled', models.CharField(choices=[('1', 'None'), ('2', '1-25%'), ('3', '26-50%'), ('4', '51-75%'), ('5', '76-100%'), ('O', 'Not applicable because we provide services')], max_length=1, verbose_name='3.2. What proportion of your packaging is made of recycled materials?')),
                ('product_recyclable', models.CharField(choices=[('1', 'Yes, fully biodegradable or recyclable'), ('2', 'Partially biodegradable or recyclable'), ('3', 'Neither'), ('4', 'Not applicable because we provide services')], max_length=1, verbose_name='3.3. Are your products biodegradable or recyclable?')),
                ('env_measure_freq', models.CharField(choices=[('1', 'Monthly'), ('2', 'Every 6 months'), ('3', 'Annually'), ('4', 'Every 3 to 5 years'), ('5', 'Never')], max_length=1, verbose_name='3.4. How often do you measure your environmental performance in the organisation?')),
                ('env_comp_freq', models.CharField(choices=[('0', 'None'), ('1', 'Once'), ('2', 'Twice'), ('3', 'Three times'), ('4', 'Four times'), ('5', 'Five times')], max_length=1, verbose_name='3.5. How many times in the last 5 years has the company entered a competition for the best environmental practices and initiatives?')),
                ('local_invest_freq', models.CharField(choices=[('0', 'Never'), ('1', '1 - 2 times'), ('2', '3 - 5 times'), ('3', 'More than 5 times')], max_length=1, verbose_name='4.1. How many times in the last 5 years has your company invested (financially or through volunteering) in local community projects?')),
                ('local_sup_proportion', models.CharField(choices=[('0', '0%'), ('1', '1 - 25%'), ('2', '26 - 50%'), ('3', '51 - 75%'), ('4', '76 - 100%'), ('N', 'Not applicable because we provide services')], max_length=1, verbose_name='4.2.What proportion of your contracts involve local suppliers?')),
                ('female_employee_proportion', models.CharField(choices=[('0', '0%'), ('1', '1 - 25%'), ('2', '26 - 50%'), ('3', '51 - 75%'), ('4', '76 - 100%')], max_length=1, verbose_name="4.3. What proportion of your company's management are women?")),
                ('disable_employee_proportion', models.CharField(choices=[('0', '0%'), ('1', '1 - 25%'), ('2', '26 - 50%'), ('3', '51 - 75%'), ('4', '76 - 100%')], max_length=1, verbose_name="4.4. What proportion of your company's workforce are registered disabled?")),
                ('social_comp_freq', models.CharField(choices=[('0', 'None'), ('1', 'Once'), ('2', 'Twice'), ('3', 'Three times'), ('4', 'Four times'), ('5', 'Five times')], max_length=1, verbose_name='4.5. How many times in the last 5 years has the company entered a competition on best social practices and initiatives?')),
                ('sus_regualtion_monitor_freq', models.CharField(choices=[('1', 'Yes, monthly'), ('2', 'Yes, every 6 months'), ('3', 'Yes, yearly'), ('0', 'No'), ('N', 'I don’t know')], max_length=1, verbose_name='5.1. Does the company regularly monitor changes in legislation and regulations related to sustainability aspects in business?')),
                ('sus_agenda', models.CharField(choices=[('1', 'Yes'), ('0', 'No'), ('N', 'I don’t know')], max_length=1, verbose_name='5.2. Is the sustainability agenda included in the company’s strategy?')),
                ('sus_annual_report', models.CharField(choices=[('1', 'Yes'), ('0', 'No'), ('N', 'I don’t know')], max_length=1, verbose_name='5.3. Does the company produce an annual sustainability report?')),
                ('sus_in_annual_report', models.CharField(choices=[('1', 'Yes'), ('0', 'No'), ('N', 'I don’t know'), ('2', 'The company doesn’t produce an annual report.')], max_length=1, verbose_name='5.4. If the company doesn’t produce an annual sustainability report, is a sustainability section included in the company’s annual report?')),
                ('sus_plan_target', models.CharField(choices=[('1', 'Yes'), ('0', 'No'), ('N', 'I don’t know')], max_length=1, verbose_name='5.5. Does the company set sustainability targets to be achieved each year?')),
                ('sus_comp_freq', models.CharField(choices=[('0', 'None'), ('1', 'Once'), ('2', 'Twice'), ('3', 'Three times'), ('4', 'Four times'), ('5', 'Five times')], max_length=1, verbose_name='5.6. How many times in the last 5 years has the company entered a competition on best sustainability or ESG practices and initiatives?')),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='avsapp.client')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aggrement_plociy', models.BooleanField(default=False)),
                ('aggrement_service', models.BooleanField(default=False)),
                ('linkedin_url', models.URLField(blank=True, verbose_name='LinkedIn Profile URL')),
                ('business_name', models.CharField(max_length=200, verbose_name='Business Name')),
                ('business_address', models.CharField(blank=True, max_length=200, verbose_name='Business Address')),
                ('location', location_field.models.plain.PlainLocationField(max_length=63)),
                ('business_email', models.EmailField(max_length=254, verbose_name='Business Emai')),
                ('business_phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Business Phone Number')),
                ('company_role', models.CharField(max_length=200, verbose_name='What is your role in the company?')),
                ('edu_cert', models.TextField(verbose_name='What is your role in the company?')),
                ('prof_member', models.TextField(verbose_name='Membership of professional bodies')),
                ('sus_work_exp', models.CharField(choices=[('1', '0-2 years'), ('2', '3-5 years'), ('3', '6-10 years'), ('4', '11 + years')], max_length=1, verbose_name='How long have you been working in the sustainability consultancy industry?')),
                ('sus_pre_work', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1, verbose_name='Have you worked for large consultancy companies such as ERM, Arup, Jacobs etc?')),
                ('sus_pre_work_details', models.TextField(blank=True, verbose_name='If you answered Yes, please specify the name of the consultancy, time frame, your job title, and your role in any projects you were involved with.')),
                ('specialisation', models.TextField(max_length=1000, verbose_name='Specialisation (please, describe areas of your expertise in which you offer services)')),
                ('prof_biography', models.TextField(max_length=1000, verbose_name='Please, provide a brief professional biography including previous employment and projects/work in the field of sustainability. (200 words max)')),
                ('vetted', models.BooleanField(default=False)),
                ('rating', models.DecimalField(decimal_places=2, default=5.0, max_digits=3)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
