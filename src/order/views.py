from django.shortcuts import render
from . import models
from .forms import OrderForm
from profiles.models import Profiles
from profiles.models import User
from django.views.generic.edit import UpdateView
from .models import Order
from django.urls import reverse_lazy
from cart.views import get_cart
from cart.models import BooksInCart
from django.contrib.messages.views import SuccessMessageMixin

class Order(SuccessMessageMixin, UpdateView):
    model=models.Order
    template_name='order/order.html'
    form_class=OrderForm

    def get_success_message(self,*args, **kwargs):
        return f"Заказ сформирован, менеджер свяжется с вами в ближайшее время"
    
    #user=request.user
    def get_object(self):
        user=self.request.user
        if user.is_authenticated and not user.is_superuser:
            user_pk=user.pk
            profile=Profiles.objects.get(user=user_pk)
            phone=profile.phone
            adress=profile.adress
        else:
            phone=''
            adress=''
        print(user.pk)
        cart=get_cart(self.request)
        obj, create=self.model.objects.get_or_create(
            cart=cart,
            contact_phone=phone,
            delivery_adress=adress,

       )


        return obj

    def get_success_url(self):
       return reverse_lazy('main')
