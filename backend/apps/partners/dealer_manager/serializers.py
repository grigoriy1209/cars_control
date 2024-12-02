from rest_framework import serializers

from apps.partners.dealer_manager.models import DealerManager


class DealerManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerManager
        fields = '__all__'
