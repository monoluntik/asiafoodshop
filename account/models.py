from django.db import models


class Order(models.Model):
    email = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13)
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    street = models.CharField(max_length=150)
    home_number = models.CharField(max_length=10)
    zip = models.CharField(max_length=15)

    def __str__(self):
        return self.name

        