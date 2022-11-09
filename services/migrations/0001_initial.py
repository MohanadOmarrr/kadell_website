# Generated by Django 4.1.1 on 2022-11-09 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=100)),
                ('body', models.TextField(blank=True, default=0, max_length=1000, null=True)),
                ('image', models.ImageField(default=0, upload_to='images/')),
                ('banner', models.ImageField(default=0, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='ServicesProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=0, max_length=100)),
                ('image', models.ImageField(default=0, upload_to='images/')),
                ('prices', models.TextField(default=0, max_length=1000)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
            ],
        ),
    ]
