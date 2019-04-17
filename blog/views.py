from rest_framework import generics, authentication, filters
from django_filters import rest_framework as filters2

from . import serializers
from .filters import PostFilter
from .models import Post
from .permissions import PostPermissions


class PostView(generics.ListCreateAPIView):
    """List every post"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (PostPermissions,)
    serializer_class = serializers.PostSerializer
    filter_backends = (filters.OrderingFilter, filters2.DjangoFilterBackend,)
    filterset_class = PostFilter
    ordering_fields = ('created_date', 'title', 'is_published')
    ordering = ('-created_date',)
    queryset = Post.objects.all()

    def _params_to_ints(self, qs):
        """Convert a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        """Retrieve only published posts for non staff users"""
        queryset = self.queryset.all()

        has_permissions = self.request.user.is_active and \
            self.request.user.is_staff
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

    def get_queryset(self):
        """Retrieve only published posts for non staff users"""
        queryset = self.queryset.all()

        has_permissions = self.request.user.is_active and \
            self.request.user.is_staff
        if not has_permissions:
            queryset = queryset.filter(is_published=True)

        return queryset


class PostImageView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the post image"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (PostPermissions,)
    serializer_class = serializers.PostImageSerializer
    queryset = Post.objects.all()
