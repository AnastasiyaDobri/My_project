from django.db import models
from cart.models import Cart
class Order(models.Model):
    cart=models.OneToOneField(
        Cart,
        on_delete=models.PROTECT
    )
    status=models.CharField(
        choices=[
        ('0','Отменен'),
        ('1','Новый'),
        ('2','Подтвержден'),
        ('3','В обработке'),
        ('4','Доставляется'),
        ('5','Доставлен'),],
        #choices=STATUS_CHOICES,
        max_length=1,
        default=('1','Новый'),
        blank=True,
    )
    delivery_adress=models.TextField("Адрес доставки", max_length=120)
    contact_phone=models.TextField("Номер телефона", max_length=40)
    created=models.DateTimeField(("Created"), auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(("Updated"), auto_now=True, auto_now_add=False)
