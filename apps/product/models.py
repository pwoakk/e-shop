from django.db import models

from apps.user.models import CustomUser


class Category(models.Model):
    name = models.CharField('Category name', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField('Name', max_length=255)
    description = models.TextField('Description')
    pictures = models.ImageField('Pictures',
                                 blank=True,
                                 null=True,
                                 upload_to='product_images/',
                                 default='default_product_image.png')
    price = models.DecimalField('Price', max_digits=19, decimal_places=2, default=0)
    discount = models.DecimalField('Discount', max_digits=3, decimal_places=0, default=0)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,
                                 verbose_name='Category',
                                 on_delete=models.CASCADE,
                                 related_name='products',
                                 null=True)
    supplier = models.ForeignKey(CustomUser,
                                 verbose_name='Supplier',
                                 on_delete=models.CASCADE,
                                 related_name='products')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.title


