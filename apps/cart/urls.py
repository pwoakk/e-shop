from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.cart.views import CartView, CartDetailView, CartItemView, CartItemDetailView, OrderView, OrderDetailView

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("<int:pk>/", CartDetailView.as_view(), name="cart-detail"),
    path("cart-item/", CartItemView.as_view(), name="cart-item"),
    path("cart-item/<int:pk>/", CartItemDetailView.as_view(), name="cart-item-detail"),
    path("order/", OrderView.as_view(), name="cart"),
    path("order/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
]