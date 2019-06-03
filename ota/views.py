from rest_framework import generics, authentication, filters
from django_filters import rest_framework as filters2
from django.shortcuts import redirect
from django.conf import settings
from django.db.models import F

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


def sf_weekly_redirect(request, device, filename):
    Build.objects.filter(filename=filename).update(downloads=F('downloads')+1)

    response = redirect(f'{settings.SF_URL}{device}/weeklies/{filename}')
    return response


def sf_redirect(request, device, filename):
    Build.objects.filter(filename=filename).update(downloads=F('downloads')+1)

    response = redirect(f'{settings.SF_URL}{device}/{filename}')
    return response


def mirror_redirect(request, device, filename):
    Build.objects.filter(filename=filename).update(downloads=F('downloads')+1)

    response = redirect(
        f'{settings.MIRROR_URL}__private__/{device}/{filename}')
    return response


def mirror_weekly_redirect(request, device, filename):
    Build.objects.filter(filename=filename).update(downloads=F('downloads')+1)

    response = redirect(
        f'{settings.MIRROR_URL}__private__/{device}/weeklies/{filename}')
    return response
