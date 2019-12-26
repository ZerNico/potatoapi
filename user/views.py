from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from . import serializers
from .models import User
from .permissions import UserPermissions


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = serializers.UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = serializers.AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = serializers.UserManageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class ManageUserImageView(generics.RetrieveUpdateAPIView):
    """Manage the user profile image"""
    serializer_class = serializers.UserImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Manage users in the database"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (UserPermissions,)
    serializer_class = serializers.UserProfileDetailSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class UserProfileImageView(generics.RetrieveUpdateAPIView):
    """Manage the user profile image"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (UserPermissions,)
    serializer_class = serializers.UserImageSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
