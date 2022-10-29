from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from apps.product.views import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'product', ProductViewSet)
print(router.urls)

urlpatterns = [
    path('', include(router.urls)),
]