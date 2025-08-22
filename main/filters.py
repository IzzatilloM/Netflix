import django_filters
from .models import *

class MovieFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(field_name="year", lookup_expr='gte')
    end_year = django_filters.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Movie
        fields = ['name', 'start_year', 'end_year']

class ActorFilter(django_filters.FilterSet):
    birth_year = django_filters.NumberFilter(field_name="year", lookup_expr='gte')
    death_year = django_filters.NumberFilter(field_name="year", lookup_expr='lte')

    class Meta:
        model = Actor
        fields = ['name', 'birth_year', 'death_year']

class ReviewFilter(django_filters.FilterSet):
    max_rate = django_filters.NumberFilter(field_name="rate", lookup_expr='gte')
    min_rate = django_filters.NumberFilter(field_name="rate", lookup_expr='lte')

    class Meta:
        model = Review
        fields = ['comment', 'max_rate', 'min_rate']

