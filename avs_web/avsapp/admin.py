from django.contrib import admin
from .models import *
# Register your models here.
class StaffAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "business_phone", "is_staff")
    # fields = ('name', 'title')
    # exclude = ('birth_date',)
    def username(self, obj):
        return obj.user.get_username()
        

    def full_name(self, obj):
        if obj.user.get_full_name():
            return obj.user.get_full_name()
        else:
            return None
    def is_staff(self, obj):
        if obj.user.is_staff:
            return 'Yes'
        else:
            return 'No'

class ClientAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "company_name", "full_name", "business_phone")
    # fields = ('name', 'title')
    # exclude = ('birth_date',)
    def username(self, obj):
        return obj.user.get_username()

    def full_name(self, obj):
        if obj.user.get_full_name():
            return obj.user.get_full_name()
        else:
            return None

class ConsultantAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "full_name", "sus_work_exp", 'vetted', 'rating')
    # fields = ('name', 'title')
    # exclude = ('birth_date',)
    def username(self, obj):
        return obj.user.get_username()

    def full_name(self, obj):
        if obj.user.get_full_name():
            return obj.user.get_full_name()
        else:
            return None

class SustainabilityNeedsAssessmentFormAdmin(admin.ModelAdmin):
    list_display = ("id", "client_username", "client_name", "create_time")
    def client_username(self, obj):
        return obj.create_by.user.get_username()

    def client_name(self, obj):
        if obj.create_by.user.get_full_name():
            return obj.create_by.user.get_full_name()
        else:
            return None

class ClientServiceEnquiryFormAdmin(admin.ModelAdmin):
    list_display = ("id", "client_username", "client_name", "create_time")

    def client_username(self, obj):
        return obj.create_by.user.get_username()

    def client_name(self, obj):
        if obj.create_by.user.get_full_name():
            return obj.create_by.user.get_full_name()
        else:
            return None

class ServiceInvitationAdmin(admin.ModelAdmin):
    list_display = ("id", "invitation_event", "invitaiton_to", "invitation_status", "update_time")

admin.site.register(Staff, StaffAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(SustainabilityNeedsAssessmentForm, SustainabilityNeedsAssessmentFormAdmin)
admin.site.register(ClientServiceEnquiryForm, ClientServiceEnquiryFormAdmin)
admin.site.register(ServiceInvitation, ServiceInvitationAdmin)

