from django.db import models

from products.models import Product
from users.models import User


class Rating(models.Model):
    rate_choice = (
        ('0', ''),
        ('1', '*'),
        ('2', '**'),
        ('3', '***'),
        ('4', '****'),
        ('5', '*****'),

    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rate = models.CharField(max_length=5, choices=rate_choice, default='')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=250)
    date_create = models.DateTimeField(auto_now_add=True)
