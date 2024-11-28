from rest_framework import serializers

from core.services.email_service import EmailService

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar
from apps.all_cars.listings.choices.status_choice import StatusChoice
from apps.all_cars.listings.models import CarPhotoModel, CarsModel
from apps.all_cars.listings.services import CarsService


class CarPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPhotoModel
        fields = ('photo',)
        extra_kwargs = {'photo': {'required': True}}


class CarSerializer(serializers.ModelSerializer):
    photos = CarPhotoSerializer(many=True, read_only=True)
    # user = UserSerializer(read_only=False,write_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    brand = serializers.PrimaryKeyRelatedField(queryset=BrandsModel.objects.all(), )
    model = serializers.PrimaryKeyRelatedField(queryset=ModelCar.objects.all(), )

    class Meta:
        model = CarsModel

        fields = ('id', 'brand', 'model', 'year',
                  'mileage', 'price', 'currency',
                  'body_type', 'engine', 'eco_standard', 'region', 'photos',
                  'checkpoint', 'color', 'status', 'created_at', 'updated_at', 'description', "user",
                  "edit_attempts",)

        read_only_fields = ('created_at', 'updated_at', 'id', 'status', "user", "edit_attempts",)

        extra_kwargs = {'views': {'write_only': True},
                        }

    def validate(self, data):
        print(data)
        user = self.context['request'].user
        # description = data.get('description','')
        car = self.instance

        if car and car.edit_attempts >= 3:
            if car.update_status == StatusChoice.INACTIVE:
                raise serializers.ValidationError({'detail': 'you have exceeded the number of edit attempts'})
            EmailService.notify_manager(user)
        CarsService.account_limit(user, data)
        CarsService.validate_foul(data.get('description',''))
        return data

    def create(self, validated_data):
        print(validated_data)
        user = self.context['request'].user
        brand = validated_data.pop('brand', None)
        if brand is None:
            raise serializers.ValidationError({'detail': 'brand is required'})
        car = CarsModel.objects.create(brand=brand, **validated_data)
        CarsService.counter_edit_attempts(car,)
        return car

    def update(self, instance, validated_data):
        description = validated_data.get('description', instance.description)
        instance.description = description
        CarsService.counter_edit_attempts(instance)
        instance.update_status(description,)
        instance.save()
        return super().update(instance, validated_data)
