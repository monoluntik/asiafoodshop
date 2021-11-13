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


