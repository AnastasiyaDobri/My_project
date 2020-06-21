from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.template import Context
from profiles.models import Profiles
from .forms import CreateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView



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