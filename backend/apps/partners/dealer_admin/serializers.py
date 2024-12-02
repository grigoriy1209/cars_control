from rest_framework.serializers import ModelSerializer

from apps.partners.dealer_admin.models import DealerAdminModel


class DealerAdminSerializer(ModelSerializer):
    class Meta:
        model = DealerAdminModel
        fields = '__all__'
