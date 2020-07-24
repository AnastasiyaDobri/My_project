# Generated by Django 3.0.6 on 2020-07-23 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_auto_20200721_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'Новый'), ('2', 'Подтвержден'), ('3', 'В обработке'), ('4', 'Доставляется'), ('5', 'Доставлен'), ('6', 'Отменен')], max_length=1),
        ),
    ]
