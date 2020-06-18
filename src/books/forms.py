from django import forms
#from .models import Genre
from .models import Books


class CreateBookForm(forms.ModelForm):
  class Meta:
      model=Books
      fields=(
          'name',
          'genre',
          'author',
          'price',
          'description',
          'image',
          'series',
          'pub_year',
          'pages',
          'rate',
          'cover',
          'forma',
          'ISBN',
          'publisher',
          'wight',
          'age',
          'available'

      )