from django import forms
#from .models import Genre
from profiles.models import Profiles
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CreateProfileForm(forms.ModelForm):
  class Meta(UserCreationForm):
      model=Profiles
      fields=(
          'user',
          'phone',
          'adress'
      )
