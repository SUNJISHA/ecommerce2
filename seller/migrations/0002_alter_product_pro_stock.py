# Generated by Django 4.1.3 on 2022-12-17 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pro_stock',
            field=models.IntegerField(),
        ),
    ]
