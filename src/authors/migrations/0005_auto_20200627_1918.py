# Generated by Django 3.0.6 on 2020-06-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20200627_1910'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'ordering': ['name']},
        ),
    ]
