from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # 他のフィールドの定義
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # ここでrelated_nameを指定
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # ここでrelated_nameを指定
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )