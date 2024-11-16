from django_filters import rest_framework as filters

from apps.listings.choices import StatusChoice
from apps.listings.models import CarsModel


class CarFilter(filters.FilterSet):

    brand_icontains = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    model_icontains = filters.CharFilter(field_name='model', lookup_expr='icontains')
    region_icontains = filters.CharFilter(field_name='region', lookup_expr='icontains')
    color_icontains = filters.CharFilter(field_name='color', lookup_expr='icontains')

    currency = filters.ChoiceFilter(field_name='currency', choices=StatusChoice.choices)
    body_type = filters.ChoiceFilter(field_name='body_type', choices=StatusChoice.choices)
    engine = filters.ChoiceFilter(field_name='engine', choices=StatusChoice.choices)
    eco_standard = filters.ChoiceFilter(field_name='eco_standard', choices=StatusChoice.choices)
    checkpoint = filters.ChoiceFilter(field_name='checkpoint', choices=StatusChoice.choices)
    status = filters.ChoiceFilter(field_name='status', choices=StatusChoice.choices)

    price = filters.RangeFilter(field_name='price')
    year = filters.RangeFilter(field_name='year')
    mileage = filters.RangeFilter(field_name='mileage')

    brand_exact = filters.CharFilter(field_name='brand', lookup_expr='exact')
    model_exact = filters.CharFilter(field_name='model', lookup_expr='exact')

    order = filters.OrderingFilter(fields=(
        ('brand', 'brand'),
        ('model', 'model'),
        ('year', 'year'),
        ('price', 'price'),
        ('mileage', 'mileage'),
        ('currency', 'currency'),
        ('body_type', 'body_type'),
        ('engine', 'engine'),
        ('eco_standard', 'eco_standard'),
        ('checkpoint', 'checkpoint'),
        ('color', 'color'),
        ('status', 'status'),
        ('region', 'region'),
        ('created_at', 'created_at'),
        ('updated_at', 'updated_at'),
    ))


