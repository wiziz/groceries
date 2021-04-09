from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import products
from django.contrib.auth.models import Group, User


class OrderForm(ModelForm):
    class Meta:
        model = products
        fields = '__all__'


user_type = ((1, 'Customer'), (2, 'Retailer'), (3, 'Wholesaler'))


class CreateUserForm(UserCreationForm):

    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
    postal_code = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'group', 'postal_code']
