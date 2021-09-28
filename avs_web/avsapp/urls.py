from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

urlpatterns = [
     path('', views.index, name='index'),

     #SNAF URL
     path('client/snaf/', views.protected_snaf_view, name='snaf'),
     path('client/snaf_start/', views.snaf_start, name='snaf_start'),

     #ECSF URL
     path('client/ecsf/', views.protected_ecsf_view, name= 'ecsf'),
     path('client/invitations/', views.client_invitations, name= 'client_invitations'),
     path('client/invitation/<uuid:invitation_id>/', views.client_invitation_details, name= 'client_invitation_details'),

     #consultant URL
     path('consultant/invitations/', views.consultant_invitations, name= 'consultant_invitations'),
     path('consultant/invitation/<uuid:invitation_id>', views.consultant_invitation_details, name= 'consultant_invitation_details'),

     #authentication url
     path('login/', views.user_login, name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name = 'avsapp/logged_out.html'),
          name ='logout'),
     path('password_change/', auth_views.PasswordChangeView.as_view(template_name = 'avsapp/password_change_form.html'),
          name = 'password_change'),
     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name = 'avsapp/password_change_done.html'),
          name = 'password_change_done'),

     # reset password urls
     path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'avsapp/password_reset_form.html'),
          name = 'password_reset'),
     path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'avsapp/password_reset_done.html'),
          name = 'password_reset_done'),
     path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'avsapp/password_reset_confirm.html'),
          name = 'password_reset_confirm'), 
     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name= 'avsapp/password_reset_complete.html'),
          name = 'password_reset_complete'),

     # register as staff, client, consultant
     path('register/staff/', views.register_staff, name='register_staff'),
     path('register/client/', views.register_client, name='register_client'),
     path('register/conslutant/', views.register_consultant, name='register_consultant'),
     # client and staff email authentication
     path('activate/<uidb64>/<token>/', views.activate, name='activate'),

     # view edit client, consultant profile
     path('edit/client/', views.edit_client, name='edit_client'),

     # path('view/consultant/', views.view_consultant, name='view_consultant'),     
     path('edit/consultant/', views.edit_consultant, name='edit_consultant'),

    
]