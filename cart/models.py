from django.db import models


# Create your models here.
class Cart(models.Model):
    title = models.CharField(max_length=100, default=0)
    image = models.ImageField(upload_to='images/', default=0)
    prices = models.TextField(max_length=1000, default=0)
