from django.shortcuts import render
from django.views.generic import ListView

from main.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'
