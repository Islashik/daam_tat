from django.db import models
from backend.apps.accounts.models import User


class Product(models.Model):

    name = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Фото', upload_to='product_images/')
    ingredients = models.CharField('Ингриденты', max_length=100)
    is_active = models.BooleanField('Активный', default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


