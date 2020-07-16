from django import forms
#from .models import Genre
from .models import Order


class OrderForm(forms.ModelForm):
  class Meta:
      model=Order
      fields=(
        'contact_phone',
       'delivery_adress',
      )
