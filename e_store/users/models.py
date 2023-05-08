from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager, AbstractUser


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthday = models.DateField(null=True)
    phone = models.IntegerField(null=True)
    order_count = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = UserManager()

    def __str__(self):
        return f"{self.username} - {self.email}"

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
