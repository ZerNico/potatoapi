import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractUser


def user_image_file_path(instance, filename):
    """Generate file path for new user image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/', filename)


class User(AbstractUser):
    device = models.CharField(max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    country = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(null=True, upload_to=user_image_file_path)
