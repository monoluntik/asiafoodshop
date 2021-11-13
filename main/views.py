from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.checks import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import *
from .forms import *


class CategoryListView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'


class ProductListView(ListView):
    model = Product
    template_name = 'main/product_list.html'
    context_object_name = 'products'
    paginate_by = 2

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
    success_url = reverse_lazy('home')

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
        print(queryset)
        return queryset

class About(TemplateView):
    template_name = 'about.html'



class Filter1View(ListView):
    model = Product
    temlate_name = 'filter/filter1.html'
    context_object_name = 'results1'

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.filter(price__range=(50, 100)):
            queryset = queryset.filter(price__range=(50, 100))
        else:
            queryset = Product.objects.none()
        print(queryset)
        return queryset


class Filter2View(ListView):
    model = Product
    temlate_name = 'filter/filter2.html'
    context_object_name = 'results2'

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.filter(price__range=(100, 200)):
            queryset = queryset.filter(price__range=(100, 200))
        else:
            queryset = Product.objects.none()
        print(queryset)
        return queryset

class Filter3View(ListView):
    model = Product
    temlate_name = 'filter/filter3.html'
    context_object_name = 'results3'

    def get_queryset(self):
        queryset = super().get_queryset()
        if queryset.filter(price__range=(200, 1000)):
            queryset = queryset.filter(price__range=(200, 1000))
        else:
            queryset = Product.objects.none()
        print(queryset)
        return queryset


@login_required()
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required()
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required()
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required()
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required()
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required()
def cart_detail(request):
    return render(request, 'cart_detail.html')

class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    success_url = reverse_lazy('home')

