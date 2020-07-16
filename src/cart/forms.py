from django import forms
#from .models import Genre
from .models import BooksInCart


class AddBookToCartForm(forms.ModelForm):
  class Meta:
      model=BooksInCart
      fields=(
        'book',
       'quantity',
      )
