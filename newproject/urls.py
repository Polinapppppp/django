from django.urls import path
from . import views
from .views import ProductListView, contact_view, contact_success

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success'),
]