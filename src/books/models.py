from django.db import models
from testapp.models import Genre

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


    def __str__(self):
        return self.name