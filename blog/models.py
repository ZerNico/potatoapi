import uuid
import os
import sys
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.text import slugify
from io import BytesIO
from PIL import Image


def post_image_file_path(instance, filename):
    """Generate file path for new post image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/post/', filename)


class Post(models.Model):
    """Post object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField(max_length=2000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    image = models.ImageField(null=True, upload_to=post_image_file_path)

    def save(self, *args, **kwargs):
        """Change values before saving"""

        # generate slug
        if not self.id:
            print('test')
        if not self.slug and not self.id:
            self.slug = slugify(self.title)

        # Resize image and reduce quality
        previous = Post.objects.filter(id=self.id).first()
        if not previous and self.image or \
                self.image and self.image != previous.image:
            res = 1024
            ext = self.image.name.split('.')[-1]
            im = Image.open(self.image)
            output = BytesIO()

            if im.width < 1024:
                res = im.width

            if ext != 'jpg' or 'jpeg':
                im = im.convert('RGB')

            ratio = (res / float(im.size[0]))
            hight = int((float(im.size[1]) * float(ratio)))
            im = im.resize((res, hight), Image.ANTIALIAS)
            im.save(output, format='JPEG', quality=70)
            output.seek(0)
            self.image = InMemoryUploadedFile(
                output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0],
                'image/jpeg', sys.getsizeof(output), None)

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
