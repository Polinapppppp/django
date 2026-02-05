from django.test import TestCase
from .models import Category, Product
from .services import get_product_data

class ProductServiceTest(TestCase):
    def test_get_product_data(self):
        category = Category.objects.create(name="Фрукты")
        Product.objects.create(name="Банан", price=45.00, category=category)

        data = get_product_data()

        self.assertEqual(len(data['categories']), 1)
        self.assertEqual(len(data['products']), 1)
        self.assertEqual(data['products'][0].name, "Банан")
        self.assertEqual(data['products'][0].category.name, "Фрукты")