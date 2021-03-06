from django.urls import path
from cart.views import AddBookToCart, CartTotal, DeleteCart, DetailCart
app_name="cart"

urlpatterns = [

    path('add/', AddBookToCart.as_view(), name='add'),
    path('cart/', CartTotal.as_view(), name='cart'),
    path('delete/<int:pk>', DeleteCart.as_view(), name='delete'),
    path('detail/<int:pk>', DetailCart.as_view(), name='detail'),

]