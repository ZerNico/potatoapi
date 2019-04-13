import tempfile
import os

from PIL import Image

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Post

from blog.serializers import PostSerializer


POSTS_URL = reverse('blog:post-list')


def detail_url(post_id):
    """Return post detail URL"""
    return reverse('blog:post-detail', args=[post_id])


def image_upload_url(post_id):
    """Return URL for post image upload"""
    return reverse('blog:post-upload-image', args=[post_id])


def sample_post(user, **params):
    """Create and return a sample post"""
    defaults = {
        'title': 'Sample post',
        'body': 'Sample body',
    }
    defaults.update(params)

    return Post.objects.create(user=user, **defaults)


class PublicBlogApiTests(TestCase):
    """Test unauthenticated blog API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'ZerNico'
            'test@potatoproject.co',
            'testpass'
        )

    def test_retrieve_posts(self):
        """Test retrieving list of posts"""
        sample_post(user=self.user)
        sample_post(user=self.user)

        res = self.client.get(POSTS_URL)

        posts = Post.objects.all().order_by('-created_date')
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)


class PrivateBlogApiTests(TestCase):
    """Test authenticated post API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
            'ZerNico',
            'test@potatoproject.co',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_create_basic_post(self):
        """Test creating post"""
        payload = {
            'title': 'Test post',
            'body': 'test body',
        }
        res = self.client.post(POSTS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)


class PostImageUploadTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_superuser(
            'ZerNico',
            'test@potatoproject.co',
            'testpass'
        )
        self.client.force_authenticate(self.user)
        self.post = sample_post(user=self.user)

    def tearDown(self):
        self.post.image.delete()

    def test_upload_image_to_post(self):
        """Test uploading an image to post"""
        url = image_upload_url(self.post.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image': ntf}, format='multipart')

        self.post.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.post.image.path))

    def test_upload_image_bad_request(self):
        """Test uploading an invalid image"""
        url = image_upload_url(self.post.id)
        res = self.client.post(url, {'image': 'notimage'}, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
