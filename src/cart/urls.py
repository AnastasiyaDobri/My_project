from django.urls import path
from cart.views import AddBookToCart, CartTotal
app_name="cart"

urlpatterns = [

    path('add/', AddBookToCart.as_view(), name='add'),
    path('cart/<int:pk>', CartTotal.as_view(), name='cart'),

]