from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import redirect


from .models import *
from .forms import CreateProductForm

class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category__slug=self.kwargs.get('slug'))
        return queryset


class DetailListView(DetailView):
    model = Product
    template_name = 'detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'create.html'
    form_class = CreateProductForm

