
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .forms import ContactForm
from .services import get_product_data
from django.views.generic import ListView
from .models import Product


class ProductListView(ListView):
    model=Product
    template_name='product_list.html'
    context_objects_name='products'
    paginate_by=5

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_success(request):
    return render(request, 'contact_success.html')