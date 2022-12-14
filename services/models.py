from django.db import models


# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100, default=0)
    body = models.TextField(max_length=1000, null=True, blank=True, default=0)
    image = models.ImageField(upload_to='images/', default=0)
    banner = models.ImageField(upload_to='images/', default=0)

    def products_list(self):
        return self.products.split(',')

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.title


class ServicesProduct(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default=0)
    prices = models.TextField(max_length=1000, default=0)

    def __str__(self):
        return f"{self.service} - {self.title}"
