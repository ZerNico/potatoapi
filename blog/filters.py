from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    created_date__lt = filters.DateFilter(
        field_name='created_date', lookup_expr='lt',
        label='Date joined is before (mm/dd/yyyy):')
    created_date__gt = filters.DateFilter(
        field_name='created_date', lookup_expr='gt',
        label='Date joined is after (mm/dd/yyyy):')
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = [
            'is_published', 'created_date', 'title', 'user'
        ]
