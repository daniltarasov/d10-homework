# Generated by Django 2.2.6 on 2020-09-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=30, verbose_name='Цвет'),
        ),
        migrations.AlterField(
            model_name='car',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=255, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=255, verbose_name='Модель'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_of_manufacture',
            field=models.IntegerField(default=1900, verbose_name='Год выпуска'),
        ),
    ]
