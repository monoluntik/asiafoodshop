from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('<str:slug>/', ProductListView.as_view(), name='list'),
    path('product/<int:product_id>/', ProductDetailListView.as_view(), name='detail'),
    path('product/create/', ProductCreateView.as_view(), name='create'),
    path('product/update/<int:product_id>/', ProductUpdateView.as_view(), name='update'),
    path('product/delete/<int:product_id>/', ProductDeleteView.as_view(), name='delete'),
    path('search', SearchListView.as_view(), name='search'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
