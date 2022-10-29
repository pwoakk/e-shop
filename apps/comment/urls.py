from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.comment.views import CommentViewSet


router = DefaultRouter()
router.register(r'', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]