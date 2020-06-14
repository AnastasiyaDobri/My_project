from django import forms
#from .models import Genre
from .models import Books


class CreateBookForm(forms.ModelForm):
  class Meta:
      model=Books
      fields=(
          'name',
          'description',
          'genre'
      )