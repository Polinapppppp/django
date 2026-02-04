from django.shortcuts import render
from .models import Category, Product

# Create your views here.
def get_product_data():
    categories = Category.objects.all()
    products = Product.objects.select_related('category').all()
    return {
        'categories': categories,
        'products': products
    }