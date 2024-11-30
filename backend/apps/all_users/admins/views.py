from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from core.permissions.is_superuser_permission import IsSuperUser

from apps.all_users.users.choices import UserRoleType
from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


class UserBanView(GenericAPIView):
    permission_classes = [IsSuperUser]
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_active:
            user.is_active = False
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserUnbanView(GenericAPIView):
    permission_classes = [IsSuperUser, ]
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if not user.is_active:
            user.is_active = True
            user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserToManagerView(GenericAPIView):
    permission_classes = [IsSuperUser]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()

        if user.role_type == UserRoleType.OWNER:
            user.role_type = UserRoleType.MANAGER

        if not user.is_staff:
            user.is_staff = True

            # user.account_type = AccountType.BASIC
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ManagerToUserView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def get_queryset(self):
        return super().get_queryset().exclude(id=self.request.user.id)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        if user.is_staff:
            user.is_staff = False
        if user.role_type == UserRoleType.MANAGER:
            user.role_type = UserRoleType.OWNER
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
