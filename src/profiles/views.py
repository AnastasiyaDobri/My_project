from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.template import Context
from profiles.models import Profiles
from .forms import CreateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView


class CreateProfile(CreateView):
    model=Profiles
    form_class=CreateProfileForm
    template_name='profiles/create_profiles.html'
    def get_success_url(self):
       return reverse_lazy('main')

class LoginProfile(LoginView):
    template_name = 'profiles/login.html'
    def get_success_url(self):
       return reverse_lazy('main')

class LogoutProfile(LogoutView):
    template_name = 'profiles/logout.html'
    def get_success_url(self):
       return reverse_lazy('main')
    
class PasswordChange(PasswordChangeView):
    template_name = 'profiles/password_reset.html'
    def get_success_url(self):
       return reverse_lazy('main')

class PasswordReset(PasswordResetView):
    template_name = 'profiles/password_reset.html'


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'profiles/password_reset_done.html'
 

class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'profiles/password_reset_confirm.html'

class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'profiles/password_reset_complete.html'
