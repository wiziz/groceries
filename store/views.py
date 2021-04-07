from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext, Template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import products
from django import forms
# Create your views here.


class Login(LoginView):
    template_name = 'store/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def success_url(self):
        return reverse_lazy('products')


class ProductList(LoginRequiredMixin, ListView):
    model = products
    template_name = 'products_List.html'
    context_object_name = 'productsObject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productsObject'] = context['productsObject'].filter(
            user=self.request.user)
        return context


class ProductDetail(LoginRequiredMixin, DetailView):
    model = products
    template_name = 'store/product_details.html'
    context_object_name = 'details'


class CreateProduct(LoginRequiredMixin, CreateView):
    model = products
    template_name = 'store/create_Product.html'
    fields = ['name', 'description', 'price', 'photo', 'availability']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(LoginRequiredMixin, UpdateView):
    model = products
    template_name = 'store/update_Product.html'
    fields = ['name', 'description', 'price', 'photo', 'availability']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = products
    context_object_name = 'productsObject'
    template_name = 'store/delete_Product.html'
    success_url = reverse_lazy('products')
