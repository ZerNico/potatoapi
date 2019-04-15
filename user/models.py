from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    device = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
