from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


class Build(models.Model):
    """Build object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    build_date = models.IntegerField()
    build_type = models.CharField(max_length=32)
    device = models.CharField(max_length=32)
    dish = models.CharField(max_length=32)
    downloads = models.IntegerField(default=0)
    filename = models.CharField(max_length=128)
    md5 = models.CharField(max_length=64, unique=True)
    notes = models.TextField(max_length=8192, null=True, blank=True)
    size = models.IntegerField()
    url = models.CharField(max_length=256)
    version = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filename


class Note(models.Model):
    """Note object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    text = models.TextField(max_length=8192)
    device = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.device


class Changelog(models.Model):
    """Note object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    changelog = ArrayField(models.CharField(max_length=1024))
    version = models.CharField(max_length=32, unique=True)
    android_version = models.CharField(max_length=32)
    date = models.DateField()

    def __str__(self):
        return self.version
