from django.test import TestCase

from apps.product.models import Category, Product
from apps.user.models import CustomUser


class CategoryModelTest(TestCase):
    def test_model(self):
        category = Category.objects.create(name='car')
        self.assertEqual(category.__str__(), category.name)


class ProductModelTest(TestCase):
    def test_model(self):
        user = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        category = Category.objects.create(name='car')
        product = Product.objects.create(
            title='LC', supplier=user, category=category, price=200000
        )
        self.assertEqual(product.__str__(), product.title)
