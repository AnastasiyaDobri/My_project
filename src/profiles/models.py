from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class Profiles(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    first_name=models.CharField(
        verbose_name="Имя",
        null=True,
        blank=False,
        max_length=150
    )

    last_name=models.CharField(
        verbose_name="Фамилия",
        null=True,
        blank=False,
        max_length=150
    )

    phone=models.CharField(
        null=True,
        blank=True,
        max_length=150

    )


    adress=models.CharField(
        verbose_name="Адрес",
        null=True,
        blank=True,
        max_length=150
    )
    
    def __str__(self):
        return self.user.first_name
