from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.exceptions import ValidationError

import os
import zipfile
import re
import hashlib

ota_storage = FileSystemStorage(
    location=settings.OTA_ROOT, base_url=settings.OTA_URL)


def build_file_path(instance, filename):
    path = ''
    if instance.private:
        path = os.path.join('__private__',)

    path = os.path.join(path, instance.device)

    if instance.build_type == 'weekly':
        path = os.path.join(path, 'weeklies/',)

    return os.path.join(path, filename)


def validate_file_extension(value):
    if not value.name.endswith('.zip'):
        raise ValidationError(u'Only zip files are allowed')


def calculate_md5(file):
    if not file:
        return None
    md5 = hashlib.md5()
    for chunk in file.chunks():
        md5.update(chunk)
    return md5.hexdigest()


class Build(models.Model):
    """Build object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True
    )
    build = models.FileField(
        upload_to=build_file_path,
        storage=ota_storage,
        validators=[validate_file_extension]
    )
    build_date = models.IntegerField()
    build_type = models.CharField(max_length=32)
    device = models.CharField(max_length=32)
    downloads = models.IntegerField(default=0)
    filename = models.CharField(max_length=128, unique=True)
    md5 = models.CharField(max_length=64)
    private = models.BooleanField(default=False)
    size = models.IntegerField()
    version = models.CharField(max_length=32)
    created_date = models.DateTimeField(auto_now_add=True)

    def clean(self):
        """Validate zip content"""
        buildzip = zipfile.ZipFile(self.build)

        try:
            buildprop = buildzip.read('system/build.prop')
        except KeyError:
            raise ValidationError(u'Provide a rom zip')

        build_date = re.search(
            r"ro.build.date.utc=([0-9]{10})", str(buildprop))

        if not build_date and not self.build_date:
            raise ValidationError(u'Timestamp not found')

        device = re.search(r"ro\.potato\.device=(.*?)\\n", str(buildprop))

        if not device and not self.device:
            raise ValidationError(u'Device name not found')

        version = re.search(r"ro\.potato\.version=(.*?)\\n", str(buildprop))

        if not version and not self.version:
            raise ValidationError(u'Version not found')

        build_type = re.search(r"ro\.potato\.type=(.*?)\\n", str(buildprop))

        if not build_type and not self.build_type:
            raise ValidationError(u'Build type not found')

        if Build.objects.filter(filename=self.build.name).exists():
            raise ValidationError(u'Build already exists')

    def save(self, *args, **kwargs):
        """Change values before saving"""
        buildzip = zipfile.ZipFile(self.build)

        buildprop = buildzip.read('system/build.prop')

        if not self.build_date:
            build_date = re.search(
                r"ro.build.date.utc=([0-9]{10})", str(buildprop))
            self.build_date = build_date.group(1)

        if not self.device:
            device = re.search(r"ro\.potato\.device=(.*?)\\n", str(buildprop))
            self.device = device.group(1)

        if not self.version:
            version = re.search(
                r"ro\.potato\.version=(.*?)\\n", str(buildprop))
            self.version = version.group(1)

        if not self.build_type:
            build_type = re.search(
                r"ro\.potato\.type=(.*?)\\n", str(buildprop))
            self.build_type = build_type.group(1)
        if not self.id:
            self.filename = self.build.name

            self.size = self.build.size

            self.md5 = calculate_md5(self.build)

        super(Build, self).save(*args, **kwargs)

    def __str__(self):
        return self.filename
