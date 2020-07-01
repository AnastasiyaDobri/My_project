from django import forms
from .models import Authors
#from .models import Books

class CreateAuthorsForm(forms.ModelForm):
    class Meta:
      model=Authors
      fields=(
          'name',
          'biography',
          'photo'
      )

