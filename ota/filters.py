from django_filters import rest_framework as filters
from .models import Build


class BuildFilter(filters.FilterSet):
    before_date__lt = filters.NumberFilter(
        field_name='build_date', lookup_expr='lt',
        label='Build before (UTC):')

    build_date__gt = filters.NumberFilter(
        field_name='build_date', lookup_expr='gt',
        label='Build after (UTC)')

    class Meta:
        model = Build
        fields = [
            'build_type', 'device', 'private', 'version', 'user', 'size'
        ]
