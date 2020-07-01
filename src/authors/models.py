from django.db import models


class Authors(models.Model):
    name=models.CharField(
        verbose_name="Имя",
        max_length=100,
        null=True,
        blank=False,

    )
    
    biography=models.TextField(
        verbose_name="Краткая биография",
        null=True,
        blank=True   
    )
  
    photo=models.ImageField(
        verbose_name="Фото автора",
        upload_to="authors_photo",
        null=True,
        blank=True,
    )
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name