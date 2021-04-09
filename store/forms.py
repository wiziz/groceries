from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import products
from django.contrib.auth.models import User


class OrderForm(ModelForm):
    class Meta:
        model = products
        fields = '__all__'


user_type = ((1, 'Customer'), (2, 'Retailer'), (3, 'Wholesaler'))


class CreateUserForm(UserCreationForm):

    type_of_user = forms.TypedChoiceField(choices=user_type, coerce=str)
    postal_code = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1',
                  'password2', 'type_of_user', 'postal_code']
