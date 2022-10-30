from django.contrib import admin

from apps.cart.models import Cart, CartItem, Order

admin.site.register([Cart, CartItem, Order])
