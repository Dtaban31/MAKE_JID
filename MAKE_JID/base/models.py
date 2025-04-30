# base/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Custom user model
class Account(AbstractUser):
    # You can override fields or add new ones here
    groups = models.ManyToManyField(
        Group,
        related_name='account_set',  # Change from 'user_set'
        blank=True,
        help_text=AbstractUser._meta.get_field('groups').help_text,
        verbose_name=AbstractUser._meta.get_field('groups').verbose_name,
        related_query_name='account',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_set',  # Change from 'user_set'
        blank=True,
        help_text=AbstractUser._meta.get_field('user_permissions').help_text,
        verbose_name=AbstractUser._meta.get_field('user_permissions').verbose_name,
        related_query_name='account',
    )

# Event model
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='events')  # Link event to Account

    def __str__(self):
        return self.title
