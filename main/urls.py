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
    path('about', About.as_view(), name='about'),





    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart_detail'),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
