from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView



from .forms import RegistrationForm

class RegisterView(CreateView):
    model = User
    form_class = RegistrationForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('home')

class OrdersPageView(TemplateView):
    template_name = 'pay.html'
