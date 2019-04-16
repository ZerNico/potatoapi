from django_filters import rest_framework as filters
from .models import Post


class PostFilter(filters.FilterSet):
    before_date = filters.DateFilter(
        field_name='created_date', lookup_expr='lt',
        label='Date joined is before (mm/dd/yyyy):')
    after_date = filters.DateFilter(
        field_name='created_date', lookup_expr='gt',
        label='Date joined is after (mm/dd/yyyy):')
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        fields = [
            'is_published', 'before_date', 'after_date', 'created_date',
            'title', 'user'
        ]
