from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserManageSerializer(serializers.ModelSerializer):
    """Serializer for the me page"""
    class Meta:
        model = User
        fields = (
            'id', 'username', 'password', 'first_name', 'last_name', 'image',
            'is_staff', 'device', 'country', 'date_joined', 'bio', 'birth_date'
        )
        read_only_fields = ('id', 'date_joined', 'is_staff')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def update(self, instance, validated_data):
        """Update a user, setting the password correctly and return it"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user


class UserProfileDetailSerializer(serializers.ModelSerializer):
    """Serializer for the user details"""
    class Meta:
        model = User
        fields = (
            'id', 'username', 'first_name', 'last_name', 'image', 'is_staff',
            'device', 'country', 'date_joined', 'bio', 'birth_date'
        )
        read_only_fields = ('id', 'date_joined')
        extra_kwargs = {'birth_date': {'write_only': True, }}


class UserImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipe"""

    class Meta:
        model = User
        fields = ('image',)
