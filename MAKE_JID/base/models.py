from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Account(AbstractUser):
    # override the default M2M fields to give them unique reverse names
    groups = models.ManyToManyField(
        Group,
        related_name='account_set',       # change this from default 'user_set'
        blank=True,
        help_text=AbstractUser._meta.get_field('groups').help_text,
        verbose_name=AbstractUser._meta.get_field('groups').verbose_name,
        related_query_name='account',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='account_set',       # change this from default 'user_set'
        blank=True,
        help_text=AbstractUser._meta.get_field('user_permissions').help_text,
        verbose_name=AbstractUser._meta.get_field('user_permissions').verbose_name,
        related_query_name='account',
    )
