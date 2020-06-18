# Generated by Django 3.0.6 on 2020-06-16 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='ISBN',
            field=models.IntegerField(blank=True, null=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='books',
            name='age',
            field=models.FloatField(blank=True, help_text='+', null=True, verbose_name='Ограничения по возрасту'),
        ),
        migrations.AddField(
            model_name='books',
            name='cover',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Обложка'),
        ),
        migrations.AddField(
            model_name='books',
            name='forma',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Формат'),
        ),
        migrations.AddField(
            model_name='books',
            name='pages',
            field=models.IntegerField(blank=True, null=True, verbose_name='Страниц'),
        ),
        migrations.AddField(
            model_name='books',
            name='pub_year',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='Год издания'),
        ),
        migrations.AddField(
            model_name='books',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Издатель'),
        ),
        migrations.AddField(
            model_name='books',
            name='rate',
            field=models.FloatField(blank=True, help_text='✰', null=True, verbose_name='Оценка'),
        ),
        migrations.AddField(
            model_name='books',
            name='series',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Серия'),
        ),
        migrations.AddField(
            model_name='books',
            name='wight',
            field=models.FloatField(blank=True, help_text='грамм', null=True, verbose_name='Вес'),
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_pictures', verbose_name='Обложка книги'),
        ),
    ]
