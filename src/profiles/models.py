from django.db import models
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField
User=get_user_model()

class Profiles(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )
    phone=PhoneNumberField(
    null=True,
    blank=True,
    region="BY"
    )

    adress=models.CharField(
       verbose_name="Адрес",
        null=True,
        blank=True,
        max_length=150
    )
    
    def __str__(self):
        return self.user.phone
