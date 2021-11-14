import django_filters
from django import forms
from django.forms import widgets

from .models import *


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.TextInput(attrs={'class': 'form-control'}),
        'body': forms.Textarea(attrs={'class': 'form-control'}),
    }


