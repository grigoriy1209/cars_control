from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.dataclasses.user_dataclass import User
from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoverToken, SocketToken

from apps.all_users.auth.serializers import EmailSerializer, PasswordSerializer
from apps.all_users.users.serializers import UserSerializer

UserModel: User = get_user_model()


class ActivateUserView(GenericAPIView):
    """
    patch: activate user
    """
    permission_classes = (AllowAny,)

    def get_serializer_class(self):
        pass

    def patch(self, *args, **kwargs):
        token = kwargs['token']
        user = JWTService.verify_token(token, ActivateToken)
        user.is_active = True
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryPasswordRequestView(GenericAPIView):
    """
    post: reset password request
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = EmailSerializer


    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = get_object_or_404(UserModel, **serializer.data)
        EmailService.recovery_password(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class RecoveryPasswordView(GenericAPIView):
    """
    post: reset password request
    """
    permission_classes = (AllowAny,)
    serializer_class = PasswordSerializer


    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        token = kwargs['token']
        user = JWTService.verify_token(token, RecoverToken)
        user.set_password(serializer.data['password'])
        user.save()
        return Response({'detail': "your password has been reset."}, status=status.HTTP_200_OK)


class SocketTokenView(GenericAPIView):
    """"
    get: get socket token
    """
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        pass

    def get(self, *args, **kwargs):
        token = JWTService.create_token(user=self.request.user, token_class=SocketToken)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
