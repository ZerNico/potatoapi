from rest_framework import serializers

from .models import Build
from user.serializers import UserProfileDetailSerializer


class BuildSerializer(serializers.ModelSerializer):
    """Serializer for the build list"""
    class Meta:
        model = Build
        fields = (
            'id', 'user', 'url', 'build_date', 'build_type', 'device',
            'dish', 'downloads', 'filename', 'md5', 'notes',
            'size', 'version'
        )
        read_only_fields = (
            'id', 'user', 'downloads'
        )


class BuildDetailSerializer(serializers.ModelSerializer):
    """Serializer for the build details"""
    class Meta:
        model = Build
        fields = (
            'id', 'user', 'url', 'build_date', 'build_type', 'device',
            'dish', 'downloads', 'filename', 'md5', 'notes',
            'size', 'version'
        )
        read_only_fields = (
            'id', 'user'
        )
    user = UserProfileDetailSerializer(read_only=True, )
