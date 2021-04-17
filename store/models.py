from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=20)

    def __str__(self):
        return self.name
        
class products(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='images', null=True)
    availability = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_products():
        return products.objects.all()
    

