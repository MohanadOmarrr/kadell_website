# Generated by Django 4.1.1 on 2022-09-22 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_servicesproducts_image_servicesproducts_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='price',
        ),
        migrations.RemoveField(
            model_name='service',
            name='products',
        ),
    ]