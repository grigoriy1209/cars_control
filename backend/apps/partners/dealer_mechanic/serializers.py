from rest_framework import serializers

from apps.partners.dealer_mechanic.models import DealerMechanicModel


class DealerMechanicSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealerMechanicModel
        fields = '__all__'
