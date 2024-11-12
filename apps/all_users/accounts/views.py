from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser

from apps.all_users.users.choices import AccountType
from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


class UserToPremiumAccountView(GenericAPIView):
    permission_classes = [IsSuperUser, IsAdminUser, ]
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.role_type == 'Premium_Seller':
            user.account_type = AccountType.PREMIUM
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
