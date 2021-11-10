from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,
                               related_name='children')

    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
