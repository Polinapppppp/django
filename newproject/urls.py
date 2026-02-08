
from django.urls import path
from .views import ProductListView, ContactView, ContactSuccessView

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/success/', ContactSuccessView.as_view(), name='contact_success'),
]