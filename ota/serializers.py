from rest_framework import serializers

from .models import Build
from user.serializers import UserProfileDetailSerializer


class BuildSerializer(serializers.ModelSerializer):
    """Serializer for the build list"""
    class Meta:
        model = Build
        fields = (
            'id', 'user', 'build', 'build_date', 'build_type', 'device',
            'downloads', 'filename', 'md5', 'notes', 'private', 'size',
            'version'
        )
        read_only_fields = (
            'id', 'filename', 'md5', 'size', 'user', 'downloads'
        )
        extra_kwargs = {
            'build_date': {'allow_null': True, 'required': False},
            'build_type': {'allow_null': True, 'required': False},
            'device': {'allow_null': True, 'required': False},
            'notes': {'allow_null': True, 'required': False},
            'version': {'allow_null': True, 'required': False}
        }

    def validate(self, attrs):
        instance = Build(**attrs)
        instance.clean()
        return attrs


class BuildDetailSerializer(serializers.ModelSerializer):
    """Serializer for the build details"""
    class Meta:
        model = Build
        fields = (
            'id', 'user', 'build', 'build_date', 'build_type', 'device',
            'downloads', 'filename', 'md5', 'notes', 'private', 'size',
            'version'
        )
        read_only_fields = (
            'id', 'user', 'build', 'filename', 'md5', 'private', 'size'
        )
    user = UserProfileDetailSerializer(read_only=True, )
