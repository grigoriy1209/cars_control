from django.contrib.auth import get_user_model
from django.db import transaction

from rest_framework import serializers

from apps.all_users.accounts.choices import AccountType
from apps.all_users.accounts.models import AccountModels
from apps.all_users.accounts.serializers import AccountSerializer
from apps.all_users.users.choices import UserRoleType
from apps.all_users.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('id', 'name', 'surname', 'age', 'phone', 'created_at', 'updated_at')


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    account = AccountSerializer(read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id',
            'email',
            'password',
            'is_active',
            'is_staff',
            'is_superuser',
            'role_type',
            'account',
            'last_login',
            'created_at',
            'updated_at',
            'profile',
        )
        read_only_fields = (
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'role_type',
            'account',
            'last_login',
            'created_at',
            'updated_at',

        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_role_type(self, value):
        roles = [role for role in UserRoleType]
        if value not in roles:
            raise serializers.ValidationError("Invalid role type.")
        return value

    @transaction.atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')

        user = UserModel.objects.create_user(**validated_data)
        profile = ProfileModel.objects.create(**profile, user=user, )
        account, created = AccountModels.objects.get_or_create(user=user, defaults={"account_type": AccountType.BASIC})
        user.account = account
        user.save()
        return user

    def update(self, instance, validated_data):

        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        profile_data = validated_data.pop('profile', None)
        if profile_data:
            profile_instance = instance.profile
            for attr, value in profile_data.items():
                setattr(profile_instance, attr, value)
            profile_instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        role_type = validated_data.pop('role_type', None)
        if role_type:
            if role_type not in [UserRoleType.OWNER, UserRoleType.BUYER, UserRoleType.SELLER, UserRoleType.MANAGER]:
                raise serializers.ValidationError("Invalid role type")
            instance.role_type = role_type
        instance.save()
        return instance
