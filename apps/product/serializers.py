from rest_framework import serializers

from apps.product.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "description",
            "picture",
            "price",
            "discount",
            "category",
            "supplier",
            "date_creation",
        ]

        extra_kwargs = {
            "title": {"required": True},
            "description": {"required": True},
            "price": {"required": True},
            "category": {"required": True},
        }
