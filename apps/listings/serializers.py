from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from core.services.email_service import EmailService

from apps.listings.models import CarPhotoModel, CarsModel
from apps.listings.services import CarsService


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}


class CarSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=False,write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = CarsModel

        fields = ('id', 'brand', 'model', 'year',
                  'mileage', 'price', 'currency',
                  'body_type', 'engine', 'eco_standard', 'region', 'photos',
                  'checkpoint', 'color', 'status', 'created_at', 'updated_at', 'description', "user",
                  "edit_attempts")

        read_only_fields = ('created_at', 'updated_at', 'id', 'status', "user", "edit_attempts")

    def validate_description(self, value):
        return CarsService.validate_foul(value)

    def validate(self, data):
        print(data)
        user = self.context['request'].user
        car = self.instance

        if car and car.edit_attempts >= 3:
            EmailService.notify_manager(user)
            if car.update_status == 'inactive':
                raise serializers.ValidationError('bkb;bb')

        car_service = CarsService()
        car_service.account_limit(user, data)

        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        car = CarsModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        instance.counter_edit_attempts()
        instance = super().update(instance, validated_data)
        instance.update_status()
        return instance
