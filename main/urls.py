from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('product/list/<str:slug>/', ProductListView.as_view(), name='list'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('update/<int:product_id>/', ProductUpdateView.as_view(), name='update'),
    path('delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete'),
    path('product/detail/<int:product_id>/', DetailListView.as_view(), name='product-detail'),
    path('search', SearchListView.as_view(), name='search'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
