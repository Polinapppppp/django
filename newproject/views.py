from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def product_list(request):
    categories=Category.objects.all()
    products = Product.objects.select_related('category').all()
    return render(request, 'product_list.html', {
        'categories':categories,
        'products':products
    })