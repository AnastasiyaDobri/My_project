from django.db import models
from genre.models import Genre
from datetime import datetime, date, time
import pytz

# Create your models here.
class Books(models.Model):
    name=models.CharField(
        verbose_name="Название книги",
        max_length=100
    )
    genre=models.ForeignKey(
        Genre,
        on_delete=models.PROTECT,
        verbose_name="Жанр книги",
        max_length=100   
    )

    description=models.TextField(
        verbose_name="Описание книги",
        null=True,
        blank=True
    )

    image=models.ImageField(
        verbose_name="Обложка книги",
        upload_to="book_pictures",
        null=True,
        blank=True
    )

    
    author=models.CharField(
        verbose_name="Автор",
        null=True,
        blank=True,
        max_length=100
    )

    price=models.FloatField(
        verbose_name="Цена",
        null=True,
        blank=True,
        help_text="BYN"
    )

    series=models.CharField(
        verbose_name="Серия",
        null=True,
        blank=True,
        max_length=100
    )

    pub_year=models.CharField(
        verbose_name="Год издания",
        null=True,
        blank=True,
        max_length=5

    )
    pages=models.IntegerField(
        verbose_name="Страниц",
        null=True,
        blank=True,
    )
    cover=models.CharField(
        verbose_name="Обложка",
        null=True,
        blank=True,
        max_length=100
    )
    forma=models.CharField(
        verbose_name="Формат",
        null=True,
        blank=True,
        max_length=100
    )
    ISBN=models.IntegerField(
        verbose_name="ISBN",
        null=True,
        blank=True,
    )

    publisher=models.CharField(
        verbose_name="Издатель",
        null=True,
        blank=True,
        max_length=100
    )
    wight=models.FloatField(
        verbose_name="Вес",
        null=True,
        blank=True,
        help_text="грамм"
    )
    

    age=models.FloatField(
        verbose_name="Ограничения по возрасту",
        null=True,
        blank=True,
        help_text="+"
    )

    rate=models.FloatField(
        verbose_name="Оценка",
        null=True,
        blank=True,
        help_text="✰"
    )
    add_date=models.DateField(
        verbose_name="Дата добавления",
        auto_now=False,
        auto_now_add=True

   )
    update_date=models.DateField (
        verbose_name="Дата обновления",
        auto_now=True,
        auto_now_add=False
    )
   
    available=models.BooleanField(
        verbose_name="Доступен к заказу (да/нет)",
       default=True
    )



    def __str__(self):
        return self.name