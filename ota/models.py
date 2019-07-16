from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.exceptions import ValidationError

import os
import zipfile

from .utils import calculate_md5, clean_buildprop, search_for_prop

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
    notes = models.TextField(max_length=256, null=True)
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

        buildprop_clean = clean_buildprop(str(buildprop, "utf-8"))

        build_date = search_for_prop(buildprop_clean, "ro.build.date.utc")

        if not build_date and not self.build_date:
            raise ValidationError(u'Timestamp not found')

        device = search_for_prop(buildprop_clean, "ro.potato.device")

        if not device and not self.device:
            raise ValidationError(u'Device name not found')

        version = search_for_prop(buildprop_clean, "ro.potato.version")

        if not version and not self.version:
            raise ValidationError(u'Version not found')

        build_type = search_for_prop(buildprop_clean, "ro.potato.type")

        if not build_type and not self.build_type:
            raise ValidationError(u'Build type not found')

        if Build.objects.filter(filename=self.build.name).exists():
            raise ValidationError(u'Build already exists')

    def save(self, *args, **kwargs):
        """Change values before saving"""
        buildzip = zipfile.ZipFile(self.build)

        buildprop = buildzip.read('system/build.prop')
        buildprop_clean = clean_buildprop(str(buildprop, "utf-8"))

        if not self.build_date:
            build_date = search_for_prop(buildprop_clean, "ro.build.date.utc")
            self.build_date = build_date

        if not self.device:
            device = search_for_prop(buildprop_clean, "ro.potato.device")
            self.device = device

        if not self.version:
            version = search_for_prop(buildprop_clean, "ro.potato.version")
            self.version = version

        if not self.build_type:
            build_type = search_for_prop(buildprop_clean, "ro.potato.type")
            self.build_type = build_type
        if not self.id:
            self.filename = self.build.name

            self.size = self.build.size

            self.md5 = calculate_md5(self.build)

        super(Build, self).save(*args, **kwargs)

    def __str__(self):
        return self.filename
