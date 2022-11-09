from django.test import TestCase

from apps.cart.models import Cart, Order, CartItem
from apps.product.models import Category, Product
from apps.user.models import CustomUser


class CartModelTest(TestCase):
    def test_price_method(self):
        user = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        cart = Cart.objects.create(user=user)
        self.assertEqual(cart.__str__(), f"cart price: {cart.cart_price}")


class CartItemModelTest(TestCase):
    def test_cart_item_price(self):
        user = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        cart = Cart.objects.create(user=user)
        category = Category.objects.create(name='car')
        product = Product.objects.create(
            title='LC', supplier=user, category=category, price=200000
        )
        cart_item = CartItem.objects.create(product=product, cart=cart, quantity=2)
        self.assertEqual(cart_item.cart_item_price, product.price * cart_item.quantity)


class OrderModelTest(TestCase):
    def test_total_price_method(self):
        user = CustomUser.objects.create_user(email="email@gmail.com", password="password")
        cart = Cart.objects.create(user=user)
        order = Order.objects.create(cart=cart, user=user)
        self.assertEqual(order.__str__(), f'total price: {order.total_price}')


