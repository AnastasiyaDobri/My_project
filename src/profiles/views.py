from django.shortcuts import render
from . import models
from django import forms
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.template import Context
from profiles.models import Profiles
from books.models import Books
from cart.models import BooksInCart
from profiles.models import User
from .forms import CreateProfileForm
from .forms import UserDataForm
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType 
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import PasswordChangeDoneView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetCompleteView

class MyGroups(Group):
    admin, created = Group.objects.get_or_create(name='Admin')
    customer, created = Group.objects.get_or_create(name='Customers')
    manager, created = Group.objects.get_or_create(name='Manager')
    content_type_books= ContentType.objects.get_for_model(Books)
    content_type_cart= ContentType.objects.get_for_model(BooksInCart) 
    customer.permissions.add(Permission.objects.get(codename='can_view_books',name='Can view books',content_type=content_type_books))
    customer.permissions.add(Permission.objects.get(codename='can_add_books_in_cart',name='Can add books in cart',content_type=content_type_cart))
    customer.permissions.add(Permission.objects.get(codename='can_change_books_in_cart',name='Can change books in cart',content_type=content_type_cart))
    customer.permissions.add(Permission.objects.get(codename='can_delete_books_in_cart',name='Can delete books in cart',content_type=content_type_cart))
    customer.permissions.add(Permission.objects.get(codename='can_view_books_in_cart',name='Can view books in cart',content_type=content_type_cart))


class CreateUserProfile(FormView):
    template_name = 'profiles/create_user.html'
    form_class = UserDataForm


    def form_valid(self, form):

        form_username=form.cleaned_data['username']
        form_password=form.cleaned_data['password']
        form_email=form.cleaned_data['email']
        form_first_name=form.cleaned_data['first_name']
        form_last_name=form.cleaned_data['last_name']
        form_adress=form.cleaned_data['adress']
        form_phone=form.cleaned_data['phone']
        
        if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )  

        user, create=models.User.objects.get_or_create(
            username=form_username,
            password=form_password,
            last_name=form_last_name,
            first_name=form_first_name,
            email=form_email,          
        )
        user.groups.add(Group.objects.get(name='Customers'))
        form_last_name=form.cleaned_data['last_name']
        profile, create=models.Profiles.objects.get_or_create(
            user=User.objects.get(username=form_username),
            last_name=form_last_name,
            first_name=form_first_name,
            adress= form_adress,
            phone=form_phone
        )     
        return HttpResponseRedirect('http://127.0.0.1:8000/')















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
