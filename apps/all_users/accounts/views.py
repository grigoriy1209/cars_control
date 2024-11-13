from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser

from apps.all_users.accounts.models import AccountType
from apps.all_users.users.choices import UserRoleType
# from apps.all_users.users.choices import AccountType
from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


class UserToPremiumAccountView(GenericAPIView):
    permission_classes = [IsSuperUser, IsAdminUser,]
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.role_type == UserRoleType.SELLER:
            user.role_type = UserRoleType.PREMIUM_SELLER

        account = user.account
        if account.account_type == AccountType.BASIC:
            user.account_type = AccountType.PREMIUM
            account.activate_premium_account(duration_days=14)
            serializer = UserSerializer(user)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

