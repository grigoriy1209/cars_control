from rest_framework import serializers

from apps.all_cars.listings.serializers import CarSerializer
from apps.dealerships.models import AutoSaloonModel


class AutoSaloonSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoSaloonModel
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user

        validated_data.pop('cars', None)
        auto_saloon = AutoSaloonModel(user=user, **validated_data)
        return auto_saloon
