# Generated by Django 3.0.6 on 2020-07-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='first_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='profiles',
            name='last_name',
            field=models.CharField(max_length=150, null=True, verbose_name='Фамилия'),
        ),
    ]
