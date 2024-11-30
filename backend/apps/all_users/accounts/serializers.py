from rest_framework import serializers

from apps.all_users.accounts.models import AccountModels


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModels

        fields = ('id', 'account_type', 'start_date', 'end_date', 'active')
        read_only_fields = ('id',
                            'account_type',
                            'start_date',
                            'end_date',
                            'active')
