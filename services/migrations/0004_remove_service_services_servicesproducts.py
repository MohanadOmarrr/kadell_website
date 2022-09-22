# Generated by Django 4.1.1 on 2022-09-22 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_service_services'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='services',
        ),
        migrations.CreateModel(
            name='ServicesProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.ManyToManyField(to='services.service')),
            ],
        ),
    ]