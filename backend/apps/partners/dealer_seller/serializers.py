from rest_framework import serializers

from apps.partners.dealer_seller.models import DealerSellerModel


class DealerSellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = DealerSellerModel
        fields = '__all__'
