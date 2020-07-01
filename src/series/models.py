from django.db import models


class Series(models.Model):

    name=models.CharField(
        verbose_name="Название",
        max_length=100,
        null=True,
        blank=False,
        default=0

    )
  
    description=models.TextField(
        verbose_name="Описание серии",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name