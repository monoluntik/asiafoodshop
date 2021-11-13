from .models import Category
from cart.cart import Cart
def get_categories(request):
    categories = Category.objects.filter(parent__isnull=True)
    return {'categories': categories}

def cart(request):
    return {'cart': Cart(request)}
