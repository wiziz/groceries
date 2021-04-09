from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class products(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=10000)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    photo = models.ImageField(upload_to='images', null=True)
    availability = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']


user_type = ((1, 'Customer'), (2, 'Retailer'), (3, 'Wholesaler'))


class Userdetails(models.Model):
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.TextField(max_length=10000)
    type_of_user = forms.TypedChoiceField(choices=user_type, coerce=str)
    postal_code = models.DecimalField(decimal_places=2, max_digits=20)
    phone = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['username']
