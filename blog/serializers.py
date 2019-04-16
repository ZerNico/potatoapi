from rest_framework import serializers

from .models import Post
from user.serializers import UserProfileDetailSerializer


class PostSerializer(serializers.ModelSerializer):
    """Serializer for the post list"""
    class Meta:
        model = Post
        fields = (
            'id', 'user', 'title', 'slug', 'created_date', 'modified_date',
            'image', 'is_published', 'body'
        )
        read_only_fields = ('id', 'user', 'created_date', 'modified_date')
        extra_kwargs = {
            'body': {'write_only': True, },
            'slug': {'allow_null': True, }
        }


class PostDetailSerializer(serializers.ModelSerializer):
    """Serializer for the post details"""
    class Meta:
        model = Post
        fields = (
            'id', 'user',  'title', 'slug', 'created_date', 'modified_date',
            'image', 'is_published', 'body'
        )
        read_only_fields = ('id', 'created_date', 'modified_date')
        extra_kwargs = {'slug': {'allow_null': True, }}
    user = UserProfileDetailSerializer(read_only=True, )


class PostImageSerializer(serializers.ModelSerializer):
    """Serializer for the post image"""

    class Meta:
        model = Post
        fields = ('image',)
