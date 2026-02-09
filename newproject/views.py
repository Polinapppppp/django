
from django.views.generic import ListView, FormView, TemplateView
from django.urls import reverse_lazy
from .models import Product, Contact
from .forms import ContactForm

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.select_related('category')

class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'