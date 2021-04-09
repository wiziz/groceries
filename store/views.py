from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.template import RequestContext, Template
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import products, Userdetails
from django import forms
from .forms import CreateUserForm
# Create your views here.


class Login(LoginView):

    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def success_url(self):
        return reverse_lazy('products')


class RegisterPage(FormView):
    template_name = 'registration/register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        user = form.save()
        group = form.cleaned_data['group']
        group.user_set.add(user)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('products')
        return super().get(*args, **kwargs)


class ProductList(LoginRequiredMixin, ListView):
    model = products
    template_name = 'products_List.html'
    context_object_name = 'productsObject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productsObject'] = context['productsObject'].filter(
            user=self.request.user)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['productsObject'] = context['productsObject'].filter(
                name__icontains=search_input)

            context['search_input'] = search_input
        return context


class ProductDetail(LoginRequiredMixin, DetailView):
    model = products
    template_name = 'store/product_details.html'
    context_object_name = 'details'


class CreateProduct(UserPassesTestMixin, LoginRequiredMixin, CreateView):
    def test_func(self):
        return not self.request.user.groups.filter(name='customer').exists()
    model = products
    template_name = 'store/create_Product.html'
    fields = ['name', 'description', 'price', 'photo', 'availability']
    success_url = reverse_lazy('products')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateProduct, self).form_valid(form)


class UpdateProduct(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    def test_func(self):
        return not self.request.user.groups.filter(name='customer').exists()
    model = products
    template_name = 'store/update_Product.html'
    fields = ['name', 'description', 'price', 'photo', 'availability']
    success_url = reverse_lazy('products')


class DeleteProduct(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    def test_func(self):
        return not self.request.user.groups.filter(name='customer').exists()
    model = products
    context_object_name = 'productsObject'
    template_name = 'store/delete_Product.html'
    success_url = reverse_lazy('products')
