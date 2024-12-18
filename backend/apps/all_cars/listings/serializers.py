from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar
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
                  'mileage', 'user_price', 'currency',
                  'exchange_rates', 'price_in_eur', 'price_in_usd', 'price_in_uah',
                  'eco_standard', 'region', 'photos', 'body_type', 'engine',
                  'checkpoint', 'color', 'status', 'created_at', 'updated_at', 'description', "user", 'auto_saloon',
                  "edit_attempts",)

        read_only_fields = ('created_at', 'updated_at', 'id', 'status', "user", "edit_attempts",)

        extra_kwargs = {'views': {'write_only': True},
                        }

    def validate(self, data):
        print(data)
        user = self.context['request'].user
        description = data.get('description', '')

        car = self.instance
        if any(word in description.lower() for word in CarsModel.foul_words):
            raise ValidationError({'description': 'This field cannot be empty.'})

        # if car and car.status == StatusChoice.INACTIVE:
        #     EmailService.notify_manager()
        #     raise serializers.ValidationError({'detail': 'you have exceeded the number of edit attempts'})
            
        CarsService.account_limit(user, data)
        return data

    def create(self, validated_data):
        print(validated_data)
        user = self.context['request'].user
        validated_data.pop('user', None)
        auto_saloon = validated_data.get('auto_saloon', None)
        exchange_rate = validated_data['exchange_rates']
        car = CarsModel(user=user, **validated_data)
        car.converter_price()
        car.update_status(user=user)
        return car

    def update(self, instance, validated_data):
        description = validated_data.get('description', instance.description)
        instance.description = description

        if instance.description != description:
            CarsService.counter_edit_attempts(instance)

        instance.update_status(user=instance.user)
        return super().update(instance, validated_data)
