from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='email')
    phone = models.CharField(max_length=150, verbose_name='номер телефона', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('pk',)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
