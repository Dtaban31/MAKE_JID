from django.db import models

# Create your models here.

# base/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    organization_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

class Event(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.account.organization_name}"

