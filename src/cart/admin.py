from django.contrib import admin
from cart.models import Cart, BooksInCart

admin.site.register(Cart)
admin.site.register(BooksInCart)

