import uuid
import os
import sys
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from io import BytesIO
from PIL import Image


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

    def save(self, *args, **kwargs):
        """Resize image, reduce quality and make it a square"""
        previous = User.objects.filter(id=self.id).first()
        if not previous and self.image or \
                self.image and self.image != previous.image:
            res = 1024
            ext = self.image.name.split('.')[-1]
            im = Image.open(self.image)
            output = BytesIO()

            if (im.width or im.height) < 1024:
                res = min(im.width, im.height)

            if ext != 'jpg' or 'jpeg':
                im = im.convert('RGB')

            im = im.resize((res, res), Image.ANTIALIAS)
            im.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                'image/jpeg', sys.getsizeof(output), None)

        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username
