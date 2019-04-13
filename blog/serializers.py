from rest_framework import serializers

from core.models import Post

from user.serializers import UserProfileSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id', 'title', 'user', 'created_date', 'modified_date',
            'image',
        )
        read_only_fields = ('id', 'created_date', 'modified_date', 'user', )


class PostDetailSerializer(PostSerializer):
    """Serialize a post detail"""
    class Meta(PostSerializer.Meta):
        fields = PostSerializer.Meta.fields + ('body',)

    user = UserProfileSerializer(read_only=True, )


class PostImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to post"""

    class Meta:
        model = Post
        fields = ('id', 'image')
        read_only_fields = ('id',)
