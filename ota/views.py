from rest_framework import generics, authentication, filters
from django_filters import rest_framework as filters2

from . import serializers
from .filters import BuildFilter
from .models import Build
from .permissions import BuildPermissions


class BuildView(generics.ListCreateAPIView):
    """List every build"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    serializer_class = serializers.BuildSerializer
    filter_backends = (filters.OrderingFilter, filters2.DjangoFilterBackend,)
    filterset_class = BuildFilter
    ordering_fields = ('build_date',)
    ordering = ('-build_date',)
    queryset = Build.objects.all()

    def perform_create(self, serializer):
        """Create a new build"""
        serializer.save(user=self.request.user)


class BuildDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show build details"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    serializer_class = serializers.BuildDetailSerializer
    queryset = Build.objects.all()
