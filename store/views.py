from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext, Template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import products
# Create your views here.


class ProductList(ListView):
    model = products
    template_name = 'products_List.html'
    context_object_name = 'productsObject'


class ProductDetail(DetailView):
    model = products
    template_name = 'store/product_details.html'
    context_object_name = 'details'
