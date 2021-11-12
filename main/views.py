from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Q

from .models import *
from .forms import CreateProductForm, UpdateProductForm


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
        # print(self.kwargs)
        slug = self.kwargs.get('slug')
        queryset = queryset.filter(category__slug=slug)
        return queryset


class ProductDetailListView(DetailView):
    model = Product
    template_name = 'generic.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_id'


class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser


class ProductCreateView(IsAdminCheckMixin, CreateView):
    model = Product
    template_name = 'create.html'
    form_class = CreateProductForm
    # success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ProductUpdateView(IsAdminCheckMixin, UpdateView):
    model = Product
    template_name = 'update.html'
    form_class = UpdateProductForm
    pk_url_kwarg = 'product_id'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_form'] = self.get_form(self.get_form_class())
        return context


class ProductDeleteView(IsAdminCheckMixin, DeleteView):
    model = Product
    template_name = 'delete_product.html'
    pk_url_kwarg = 'product_id'
    success_url = 'home'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect('home')


class SearchListView(ListView):
    model = Product
    template_name = 'search.html'
    context_object_name = 'results'

    def get_queryset(self):
        queryset = super().get_queryset()
        q = self.request.GET.get('q')
        if not q:
            queryset = Product.objects.none()
        else:
            queryset = queryset.filter(Q(name__icontains=q) | Q(description__icontains=q))
        return queryset

def about(request):
    return render(request, 'about.html')