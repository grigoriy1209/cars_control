from rest_framework import serializers

from apps.dealerships.models import AutoSaloonModel


class AutoSaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AutoSaloonModel
        fields = '__all__'
