from django.db import models

from users.models import User
from products.models import Product


class Order(models.Model):
    status_choice = (
        ('ready', 'ready'),
        ('in process', 'in process'),
        ('closed', 'closed')
    )
    pay_choice = (
        ('cash', 'cash'),
        ('credit_cart', 'credit_cart')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choice, default='in process')
    total_price = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=15)
    street = models.CharField(max_length=25)
    house = models.IntegerField()
    pay_method = models.CharField(max_length=20, choices=pay_choice, default='credit_cart')

    def __str__(self):
        return f"{self.user.username} - {self.status} - {self.date_create}"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='OrderItem')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.order}"
