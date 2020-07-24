from django.db import models
from cart.models import Cart
from django.db.models.signals import post_save
from django.dispatch import receiver

class Order(models.Model):
    cart=models.OneToOneField(
        Cart,
        on_delete=models.PROTECT
    )
    status=models.CharField(
        choices=[
        ('1','Новый'),
        ('2','Подтвержден'),
        ('3','В обработке'),
        ('4','Доставляется'),
        ('5','Доставлен'),
        ('6','Отменен'),],
        max_length=1,
        blank=False,
        default='1',
    )

    delivery_adress=models.CharField("Адрес доставки", max_length=120)
    contact_phone=models.CharField("Номер телефона", max_length=40)
    created=models.DateTimeField(("Created"), auto_now=False, auto_now_add=True)
    updated=models.DateTimeField(("Updated"), auto_now=True, auto_now_add=False)

#@receiver(post_save, sender=Order)
#def create_order(sender,instance,created,**kwargs):
        #instance.status='1'
        #instance.save


   
