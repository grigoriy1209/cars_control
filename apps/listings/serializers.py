from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from better_profanity import profanity

from apps.listings.models import CarPhotoModel, CarsModel


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
                  'checkpoint', 'color', 'status', 'created_at', 'updated_at', "user", "edit_count", "edit_attempts")
        read_only_fields = ('created_at', 'updated_at', 'id', 'status', "user", "edit_count", "edit_attempts")

    def validate(self, validate_data):
        instance = self.instance
        user = self.context['request'].user

        if user.account.account_type == 'Basic' and user.cars.count() >= 1:
            raise ValidationError({"detail": "Basic account allows you to place only one ad"})
        if instance and instance.edit_attempts >= 3:
            CarsModel.objects.filter(id=instance.id).update(status='inactive')
            raise ValidationError({"detail": "You cannot place more than 3 ad"})
        return validate_data

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return CarsModel.objects.create(**validated_data)
