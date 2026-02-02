
import factory
from .models import Category, Product

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker('sentence', nb_words=2)
    price = factory.Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    category = factory.SubFactory(CategoryFactory)