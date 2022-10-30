from django.test import TestCase

from apps.comment.models import Comment
from apps.product.models import Category, Product
from apps.user.models import CustomUser


class CommentModelTest(TestCase):
    def test_model(self):
        author = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        category = Category.objects.create(name='car')
        product = Product.objects.create(
            title='LC', supplier=author, category=category, price=200000
        )
        comment = Comment.objects.create(
            author=author, content='comment', product=product
        )
        self.assertEqual(comment.__str__(), f"author:{comment.author} comment:{comment.content}")
