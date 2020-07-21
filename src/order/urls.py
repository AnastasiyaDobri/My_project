from django.urls import path
from order.views import Order
from order.views import DetailOrder, DeleteOrder
app_name="order"

urlpatterns = [

    path('order/', Order.as_view(), name='order'),
    path('list/', DetailOrder.as_view(), name='list'),
    path('delete/<int:pk>', DeleteOrder.as_view(), name='delete'),


]