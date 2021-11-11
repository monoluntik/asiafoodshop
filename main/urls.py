from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('product/list/<str:slug>/', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:product_id>/', ProductUpdateView.as_view(), name='update'),
    path('detail/<str:slug>/', DetailListView.as_view(), name='detail'),
    path('delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete'),
    path('product/detail/<int:product_id>/', DetailListView.as_view(), name='product-detail'),
    path('search', SearchListView.as_view(), name='search'),
]
