from django.contrib.auth import get_user_model
from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.permissions.is_superuser_permission import IsSuperUser

from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


@method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class UserCreateView(CreateAPIView):
    """
        post:create user
    """
    serializer_class = UserSerializer
    # queryset = UserModel.objects.select_related('profile').prefetch_related('cars').all()
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    put:update user
    patch:partial update user
    delete:delete user
    """
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsSuperUser, ]


class MeInfoView(GenericAPIView):
    """
    post:get me information
    """
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated, ]

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
