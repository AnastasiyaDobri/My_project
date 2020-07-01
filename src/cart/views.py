from django.shortcuts import render
from django.contrib import admin
from . import models
from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from books.models import Books
from cart.models import BooksInCart
from cart.models import Cart
from .forms import AddBookToCartForm
from django.urls import reverse_lazy
from profiles.models import Profiles
from django.contrib.messages.views import SuccessMessageMixin

class AddBookToCart(UpdateView, SuccessMessageMixin):
    model=models.BooksInCart
    template_name='cart/add.html'
    form_class=AddBookToCartForm
    success_message =f"{book} was added to cart"
    def get_object(self):
        book_pk=self.request.GET.get('book_pk')
        cart_pk=self.request.session.get('cart_pk',0)
        book=Books.objects.get(pk=book_pk)
        user=self.request.user
        cart, create=models.Cart.objects.get_or_create(
            pk=cart_pk,
            user=user,
            defaults={}
        )
        if create:
            self.request.session['cart_pk']=cart.pk
        obj, create=self.model.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={}
       )
        return obj


    def get_success_url(self):
       return reverse_lazy('books:list')

class CartTotal(ListView):
    model=BooksInCart
    template_name='cart/cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Profiles.objects.all()
        return context
    def get_success_url(self):
       return reverse_lazy('main')