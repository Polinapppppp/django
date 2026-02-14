from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from .services import get_product_data
from .forms import ContactForm

class ProductListView(ListView):
    template_name = 'product_list.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        data = get_product_data()
        self.object_list = data['products']
        context = super().get_context_data(object_list=self.object_list)
        context['categories'] = data['categories']
        return context

class ContactView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

class ContactSuccessView(TemplateView):
    template_name = 'contact_success.html'