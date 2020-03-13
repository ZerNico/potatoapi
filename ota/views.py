from rest_framework import generics, authentication, filters
from django_filters import rest_framework as filters2

from . import serializers
from .filters import BuildFilter
from .models import Build, Note, Changelog
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


class BuildDetailHashView(BuildDetailView):
    serializer_class = serializers.BuildDetailHashSerializer
    lookup_field = 'md5'


class NoteView(generics.ListCreateAPIView):
    """List every note"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    serializer_class = serializers.NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        """Create a new build"""
        serializer.save(user=self.request.user)


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show build details"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    serializer_class = serializers.NoteDetailSerializer
    queryset = Note.objects.all()
    lookup_field = 'device'


class ChangelogView(generics.ListCreateAPIView):
    """List every changelog"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('version',)
    ordering = ('-version',)
    serializer_class = serializers.ChangelogSerializer
    queryset = Changelog.objects.all()

    def perform_create(self, serializer):
        """Create a new changelog"""
        serializer.save(user=self.request.user)


class ChangelogDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Show changelog details"""
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (BuildPermissions,)
    serializer_class = serializers.ChangelogDetailSerializer
    queryset = Changelog.objects.all()
    lookup_field = 'version'
