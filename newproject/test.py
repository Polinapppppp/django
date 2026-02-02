from django.test import TestCase
from .models import Tag
from .factories import ProductFactory
from .models import Category, Product

class TagModelTest(TestCase):
    def test_tag_creation(self):
        tag = Tag.objects.create(name="Органический")
        self.assertEqual(tag.name, "Органический")
        self.assertIsInstance(tag, Tag)



class ProductWithFixtureTest(TestCase):
    fixtures = ['categories.json']

    def test_product_with_fixture_category(self):
        fruit_category = Category.objects.get(name="Фрукты")
        product = Product.objects.create(
            name="Апельсин",
            price=70.00,
            category=fruit_category
        )
        self.assertEqual(product.category.name, "Фрукты")

class ProductWithFactoryTest(TestCase):
    def test_product_creation_with_factory(self):
        product = ProductFactory.create()
        self.assertIsNotNone(product.name)
        self.assertIsNotNone(product.price)
        self.assertIsNotNone(product.category)
        self.assertIsInstance(product.category, Category)