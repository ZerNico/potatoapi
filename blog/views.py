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
