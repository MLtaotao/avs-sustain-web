from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from .forms import *
from .models import Client, Staff, Consultant, SustainabilityNeedsAssessmentForm, 
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib.auth.decorators import login_required, user_passes_test
from formtools.wizard.views import SessionWizardView

# Create your views here.
def index(request):
    return render(request, 'avsapp/index.html')

#user login view, check whether the user is staff, client or consultant.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username = cd['username'],
                                password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #check whether the user is client or consultant or staff
                    #need to define redirected to right view
                    if hasattr(request.user, 'staff'):
                        return HttpResponseRedirect('/admin/')
                    elif hasattr(request.user, 'client'):
                        return render(request, 'avsapp/index.html')
                    elif hasattr(request.user, 'consultant'):
                        return HttpResponseRedirect('/edit/consultant/')
                    else:
                        return HttpResponse('Authenticated user '\
                                            'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse("Invalid login")
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'avsapp/login.html', {
        'form': form
    })
#if some error happens, transaction.atomic will roll back database to avoid more mistakes.
@transaction.atomic
def register_staff(request):
    if request.method == "POST":
        u_form = UserForm(request.POST, prefix= 'u_form')
        p_form = StaffForm(request.POST, prefix= 'p_form')
        if u_form.is_valid() and p_form.is_valid():

            user = u_form.save()

            p_form = p_form.save(commit= False)
            p_form.user = user
            p_form.save()

            #if we straight forwardly set the user staff status after form.save(), will have some error with registration
            user.is_staff = True
            user = user.save()

            return HttpResponse("Register staff successfully!")    

    else:
        u_form = UserForm(prefix='u_form')
        #reuse p_form in different views to complete register html
        p_form = StaffForm(prefix='p_form')
    return render(request, 'avsapp/register_staff.html', {
        'u_form' : u_form,
        'p_form' : p_form
    })

@transaction.atomic
def register_client(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ClientForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():

            user = u_form.save()

            p_form = p_form.save(commit= False)
            p_form.user = user
            p_form.save()

            #set user active status to false until the email is authenticate
            user.is_active = False
            user.save()

            #send email to client account
            current_site = get_current_site(request)
            mail_subject = 'Activate your client account.'
            message = render_to_string('avsapp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = u_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #change as wanted
            return HttpResponse('Please confirm your email address to complete the registration')

    else:
        u_form = UserForm()
        #reuse p_form in different views to complete register html
        p_form = ClientForm()
    return render(request, 'avsapp/register_client.html', {
        'u_form' : u_form,
        'p_form' : p_form
    })

@transaction.atomic
def register_consultant(request):
    if request.method == "POST":
        u_form = UserForm(request.POST)
        p_form = ConsultantForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():

            user = u_form.save()

            p_form = p_form.save(commit= False)
            p_form.user = user
            p_form.save()

            #set user active status to false until the email is authenticate
            user.is_active = False
            user.save()

            #send email to client account
            current_site = get_current_site(request)
            mail_subject = 'Activate your consultant account.'
            message = render_to_string('avsapp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user),
            })
            to_email = u_form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            #change as wanted
            return HttpResponse('Please confirm your email address to complete the registration')  

    else:
        u_form = UserForm()
        #reuse p_form in different views to complete register html
        p_form = ConsultantForm()
    return render(request, 'avsapp/register_consultant.html', {
        'u_form' : u_form,
        'p_form' : p_form
    })

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

@user_passes_test(lambda user: hasattr(user, 'client'))
def edit_client(request):
    if request.method == "POST":
        u_form = UserEditForm(instance= request.user,
                                data= request.POST)
        
        p_form = ClientEditForm(instance= request.user.client,
                                data= request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserEditForm(instance= request.user)
        p_form = ClientEditForm(instance= request.user.client)

    return render(request,'avsapp/edit_account.html',{
        'u_form': u_form,
        'p_form': p_form
    })

@user_passes_test(lambda user: hasattr(user, 'consultant'))
def edit_consultant(request):
    if request.method == "POST":
        u_form = UserEditForm(instance= request.user,
                                data= request.POST)
        
        p_form = ConsultantEditForm(instance= request.user.consultant,
                                data= request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
    else:
        u_form = UserEditForm(instance= request.user)
        p_form = ConsultantEditForm(instance= request.user.consultant)

    return render(request,'avsapp/edit_account.html',{
        'u_form': u_form,
        'p_form': p_form
    })

class SNAFWizard(SessionWizardView):
    template_name = 'avsapp/snaf_wizard_form.html'
    form_list = [SNAF1, SNAF2, SNAF3, SNAF4, SNAF5]

    def done(self, form_list, **kwargs):
        # create a snaf object to store all the values
        snaf = SustainabilityNeedsAssessmentForm()

        # set the user as the request user
        snaf.create_by = Client.objects.get(user= self.request.user)
        snaf.save()
        
        # save all the forms data to snaf
        for form in form_list:
            for key, value in form.cleaned_data.items():
                 setattr(snaf, key, value)
            snaf.save()

        return render(self.request, 'avsapp/snaf_done.html')

protected_snaf_view = user_passes_test(lambda user: hasattr(user, 'client'))(SNAFWizard.as_view())

@user_passes_test(lambda user: hasattr(user, 'client'))
def snaf_start(request):
    return render(request, 'avsapp/snaf_start.html')

class ECSFWizard(SessionWizardView):
    template_name = 'avsapp/ecsf_wizard_form.html'
    form_list = [ECSF1, ECSF2, ECSF3]

    def get_form_instance(self, step):
        return self.instance_dict.get(step, self.request.user.client)

    def done(self, form_list, **kwargs):
        # create a snaf object to store all the values
        snaf = SustainabilityNeedsAssessmentForm()

        # set the user as the request user
        snaf.create_by = Client.objects.get(user= self.request.user)
        snaf.save()
        
        # save all the forms data to snaf
        for form in form_list:
            for key, value in form.cleaned_data.items():
                 setattr(snaf, key, value)
            snaf.save()

        return render(self.request, 'avsapp/ecsf_done.html')


protected_ecsf_view = user_passes_test(lambda user: hasattr(user, 'client'))(ECSFWizard.as_view())