from django.db import models

from apps.product.models import Product
from apps.user.models import CustomUser


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, related_name='cart')
    cart_price = models.DecimalField(max_digits=19, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"cart price: {self.cart_price}"


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart')
    quantity = models.PositiveIntegerField(default=1)
    cart_item_price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return f"cart item price: {self.cart_item_price}"


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='order', blank=True)
    total_price = models.DecimalField(max_digits=19, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  f'total price: {self.total_price}'
