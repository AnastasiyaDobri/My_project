from django import forms
#from .models import Genre
from profiles.models import Profiles
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



class CreateProfileForm(forms.ModelForm):
  class Meta(UserCreationForm):
      model=Profiles
      fields=(
          'first_name',
          'last_name',
          'phone',
          'adress',
      )

class UserDataForm(forms.Form):
    username=forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=50)
    first_name=forms.CharField(max_length=150)
    last_name=forms.CharField(max_length=150)
    phone=forms.CharField(max_length=150)
    adress=forms.CharField(max_length=150)
 