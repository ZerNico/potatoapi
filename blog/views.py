from rest_framework import generics, authentication
from . import serializers
from .models import Post
from .permissions import PostPermissions


class PostView(generics.ListCreateAPIView):
    """List every post"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (PostPermissions,)
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        """Retrieve only published posts for non staff users"""
        queryset = self.queryset.all()
        has_permissions = self.request.user.is_active and self.request.user.is_staff
        if not has_permissions:
            queryset = queryset.filter(is_published=True)

        return queryset

    def perform_create(self, serializer):
        """Create a new post"""
        serializer.save(user=self.request.user)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show post details"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (PostPermissions,)
    serializer_class = serializers.PostDetailSerializer
    queryset = Post.objects.all()


class PostImageView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the post image"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (PostPermissions,)
    serializer_class = serializers.PostImageSerializer
    queryset = Post.objects.all()
