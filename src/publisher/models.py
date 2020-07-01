from django.db import models


class Publishers(models.Model):
    name=models.CharField(
        verbose_name="Название",
        max_length=100,
        null=True,
        blank=True,
        default=0
    
    )
  
    logo=models.ImageField(
        verbose_name="Логотип",
        upload_to="publisher_logo",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name