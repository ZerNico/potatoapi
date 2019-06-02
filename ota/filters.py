from django_filters import rest_framework as filters
from .models import Build


class BuildFilter(filters.FilterSet):

    class Meta:
        model = Build
        fields = [
            'private',
        ]
