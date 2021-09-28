from .models import Staff, Client, Consultant, SustainabilityNeedsAssessmentForm, ClientServiceEnquiryForm
from django.contrib.auth.models import User


# requirement_details is from form ECSF3
def search_consultants(requirement_details):

    #search consultant 3 for waiting list and 3 for backup list
    #'consult_location', 'allow_grad_consult', 'priority_consult_exp', 'priority_consult_loc',
    #        'priority_consult_cost', 'priority_project_date', 'priority_consult_rating'
    
    #only vetted consultant could be invited
    consultants = Consultant.objects.filter(vetted= True)

    #priority sort: 'priority_consult_exp', 'priority_consult_loc','priority_consult_cost', 'priority_project_date', 'priority_consult_rating'
    # priority_dict = dict()
    # for keys in ['priority_consult_exp', 'priority_consult_loc','priority_consult_cost', 'priority_project_date', 'priority_consult_rating']:
    #     priority_dict[keys] = requirement_details[keys]
    #sort the dict
    # priority_dict_sort = {k: v for k, v in sorted(priority_dict.items(), key=lambda item: item[1])}

    if requirement_details['allow_grad_consult'] == '1':
        consultants.exclude(SUS_WORK_EXP_CHOICE = '1')
    else:
        consultants = consultants.order_by('-rating', '-sus_work_exp')

    return consultants
