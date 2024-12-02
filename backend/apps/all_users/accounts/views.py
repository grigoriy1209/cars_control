from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser

from apps.all_users.accounts.models import AccountModels, AccountType
from apps.all_users.users.choices import UserRoleType
from apps.all_users.users.permissions import IsManagerOrAdmin
from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


class UserToPremiumAccountView(GenericAPIView):
    permission_classes = [IsManagerOrAdmin,]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        account = getattr(user, 'account', None)

        if not account:
            return Response({"detail":"You doesnt have an account "},status=status.HTTP_404_NOT_FOUND)

        if user.role_type != UserRoleType.SELLER:
            return Response({'detail':'Only sellers can update to premium'},status=status.HTTP_403_FORBIDDEN)

        if account.account_type == AccountType.BASIC:
            user.role_type = UserRoleType.PREMIUM_SELLER
            user.save()
            AccountModels.objects.activate_premium_account(account, duration_days=14)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "user account is already premium"}, status=status.HTTP_400_BAD_REQUEST)


class PremiumToBasicAccountView(GenericAPIView):
    permission_classes = [IsManagerOrAdmin]
    queryset = UserModel.objects.all()

    def get_serializer_class(self):
        pass

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        account = getattr(user, 'account', None)

        if not account:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user.role_type != UserRoleType.PREMIUM_SELLER:
            return Response(status=status.HTTP_403_FORBIDDEN)

        user.role_type = UserRoleType.SELLER
        user.save()

        if account.account_type == AccountType.PREMIUM:
            account.account_type = AccountType.BASIC
            account.active = False
            account.end_date = None
            account.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "User account is already Basic"}, status=status.HTTP_400_BAD_REQUEST)
