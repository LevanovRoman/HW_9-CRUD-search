# Generated by Django 4.1.1 on 2022-09-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantmodel',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
    ]