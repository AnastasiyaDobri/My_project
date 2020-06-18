from django import forms
from .models import Genre
#from .models import Books

class CreateGenreForm(forms.ModelForm):
  class Meta:
      model=Genre
      fields=(
          'name',
          'description'
      )

