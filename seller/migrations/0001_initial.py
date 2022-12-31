# Generated by Django 4.1.3 on 2022-12-17 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0005_seller_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pro_name', models.CharField(max_length=20)),
                ('pro_description', models.CharField(max_length=100)),
                ('pro_number', models.BigIntegerField()),
                ('pro_price', models.FloatField()),
                ('pro_stock', models.BigIntegerField()),
                ('pro_image', models.ImageField(upload_to='product/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.seller')),
            ],
        ),
    ]
