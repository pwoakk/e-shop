from django.db import models

from apps.product.models import Product
from apps.user.models import CustomUser


class Comment(models.Model):
    CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    author = models.ForeignKey(CustomUser,
                               verbose_name='Author',
                               on_delete=models.CASCADE,
                               related_name='comments')
    rate = models.IntegerField(choices=CHOICES, blank=True, null=True)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    replies = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"author:{self.author} comment:{self.content}"
