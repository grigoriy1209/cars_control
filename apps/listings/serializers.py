from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
                  'checkpoint', 'color', 'is_active', 'created_at', 'updated_at', 'description', "user", "edit_attempts")

        read_only_fields = ('created_at', 'updated_at', 'id', 'is_active', "user", "edit_attempts")

    def validate(self, data):
        print(data)
        user = self.context['request'].user
        add_cars = self.instance if self.instance else CarsModel(**data)

        car_service = CarsService()
        car_service.account_limit(user, data)

        description = data.get('description', '')
        CarsService.validate_foul(description)

        # if add_cars.edit_attempts >= 3:
        #     add_cars.is_active = False
        #     add_cars.save()
        #     add_cars.notify_manager()
        #     print(add_cars.notify_manager)
        #     raise ValidationError('fgfggff')
        # add_cars.is_active = True
        # add_cars.save()
        return data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        car = CarsModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance
