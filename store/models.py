from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class products(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    photo = models.ImageField(upload_to='images', null=True)
    availability = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
