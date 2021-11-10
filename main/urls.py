from django.contrib import admin
from django.urls import path, include

from .views import CategoryListView

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),

]
