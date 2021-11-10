from django.contrib import admin
from django.urls import path

from .views import CategoryListView, ProductCreateView, ProductUpdateView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:product_id>/', ProductUpdateView.as_view(), name='update'),

]
