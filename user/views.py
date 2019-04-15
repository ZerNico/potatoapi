from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import UserSerializer, AuthTokenSerializer, \
    UserProfileSerializer, UserProfileDetailSerializer, UserManageSerializer, \
    UserImageSerializer
from .models import User
from .permissions import UserPermissions


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for the user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserManageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class ManageUserImageView(generics.RetrieveUpdateAPIView):
    """Manage the user profile image"""
    serializer_class = UserImageSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


class UserProfileView(generics.ListAPIView):
    """Display all the users"""
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()


class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Manage users in the database"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (UserPermissions,)
    serializer_class = UserProfileDetailSerializer
    queryset = User.objects.all()


class UserProfileImageView(generics.RetrieveUpdateAPIView):
    """Manage the user profile image"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (UserPermissions,)
    serializer_class = UserImageSerializer
    queryset = User.objects.all()
