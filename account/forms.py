from django import forms
from django.contrib.auth.models import User
from django.core.mail import  send_mail
from django.forms.fields import CharField

from .models import Order



def send_welcome_email(email):
    message = f'Спасибо за регистрацию на нашем сайте UMAMI!'
    send_mail(
        'Welcome to UMAMI',
        message,
        'pyshop@gmail.com',
        [email],
        fail_silently=False
    )

def send_order_email(email, massage):
    send_mail(
        'Thank you for your order',
        massage,
        'pyshop@gmail.com',
        [email],
        fail_silently=False
    )


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
#     def clean(self):
#         data = self.cleaned_data
#         email = data.get('email')
#         name = data.get('name')
#         last_name = data.get('last_name')
#         address = data.get('address')
#         phone_number = data.get('phone_number')
#         country = data.get('country')
#         city = data.get('city')
#         street = data.get('street')
#         home_number = data.get('home_number')
#         zip = data.get('zip')
#         return data


    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        send_order_email(user.email, f'{user.email}\n{user.name} {user.last_name}\n{user.address}\n{user.phone_number}\n{user.country}\n{user.city} {user.zip}\n{user.street} {user.home_number}')
        return user


class RegistrationForm(forms.ModelForm):    
    password = forms.CharField(min_length=8, required=True,
                               widget=forms.PasswordInput)
    password_confirmation = forms.CharField(min_length=8, required=True,
                               widget=forms.PasswordInput)

    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirmation']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('User with such email already exist')
        return email
        
    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password_conf = data.pop('password_confirmation')
        if password != password_conf:
            raise forms.ValidationError('Password do not match')
        return data

    def save(self, commit=True):
        user = User.objects.create_user(**self.cleaned_data)
        send_welcome_email(user.email)
        return user