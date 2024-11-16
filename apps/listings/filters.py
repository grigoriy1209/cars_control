from django_filters import rest_framework as filters

from apps.listings.choices import StatusChoice


class CarFilter(filters.FilterSet):
    brand_icontains = filters.CharFilter(field_name='brand',
                                         lookup_expr='icontains')
    model_icontains = filters.CharFilter(field_name='model',
                                         lookup_expr='icontains')
    price_max = filters.NumberFilter(field_name='price', lookup_expr='lte')
    year_min = filters.NumberFilter(field_name='year', lookup_expr='gte')
    year_max = filters.NumberFilter(field_name='year', lookup_expr='lte')
    mileage_min = filters.NumberFilter(field_name='mileage', lookup_expr='gte')
    mileage_max = filters.NumberFilter(field_name='mileage', lookup_expr='lte')
    region_icontains = filters.CharFilter(field_name='region',
                                          lookup_expr='icontains')
    status = filters.ChoiceFilter(field_name='status', choices=StatusChoice.choices)
    order = filters.OrderingFilter(fields=(
        'brand', 'model', 'year', 'price', 'mileage',
        'currency', 'body_type', 'engine', 'eco_standard',
        'checkpoint', 'color', 'status', 'region', 'create_at'
    ))
