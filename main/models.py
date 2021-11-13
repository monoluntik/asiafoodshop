from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(primary_key=True)
    image = models.ImageField(upload_to='categories', blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE,
                               related_name='children')


    def __str__(self):
        if self.parent:
            return f'{self.parent} --> {self.title}'
        return self.title

    @property
    def get_children(self):
        if self.children:
            return self.children.all()
        return False


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        if self.image:
            return self.image
        return ""


class Comment(models.Model):
    post = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
