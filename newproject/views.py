

from django.shortcuts import render
from .services import get_product_data

def product_list(request):
    context = get_product_data()
    return render(request, 'product_list.html', context)