# Generated by Django 4.1.3 on 2022-12-15 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_alter_seller_seller_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='username',
            field=models.CharField(default='', max_length=20),
        ),
    ]
