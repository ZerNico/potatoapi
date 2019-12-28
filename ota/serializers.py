from rest_framework import serializers

from .models import Build, Note
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


class BuildDetailHashSerializer(BuildDetailSerializer):
    lookup_field = 'md5'


class NoteSerializer(serializers.ModelSerializer):
    """Serializer for the build list"""
    class Meta:
        model = Note
        fields = (
            'id', 'user', 'device', 'text'
        )
        read_only_fields = (
            'id', 'user'
        )


class NoteDetailSerializer(serializers.ModelSerializer):
    """Serializer for the note details"""
    class Meta:
        model = Note
        fields = (
            'id', 'user', 'device', 'text'
        )
        read_only_fields = (
            'id', 'user'
        )

    lookup_field = 'device'
    user = UserProfileDetailSerializer(read_only=True, )
