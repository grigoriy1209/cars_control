from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.services.email_service import EmailService

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar


class ModelSerializer(serializers.ModelSerializer):
    brand = serializers.SlugRelatedField(queryset=BrandsModel.objects.all(), slug_field='title', )
    class Meta:
        model = ModelCar
        fields = ('id', 'model_car', 'brand','created_at', 'updated_at')

    def validate_model_car(self, value):
        if len(value) < 2:
            EmailService.notify_admin_error_brand(value)
            raise ValidationError('The model car cannot be empty.')
        return value

    def create(self, validated_data):
        brand = validated_data.get('brand')
        if not brand:
            # EmailService.notify_admin_error_brand()
            raise ValidationError('The brands model cannot be empty.')
        model = ModelCar.objects.create( **validated_data)
        return model


class BrandSerializer(serializers.ModelSerializer):
    car_models = ModelSerializer(many=True, read_only=True)

    class Meta:
        model = BrandsModel
        fields = ('id', 'title', 'car_models', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')

    def validate_title(self, value):
        if not value:
            EmailService.notify_admin_error_brand(value)
            raise ValidationError('The title cannot be empty.')
        return value
