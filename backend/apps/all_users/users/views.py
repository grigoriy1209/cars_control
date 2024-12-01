from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.all_users.users.serializers import UserSerializer

UserModel = get_user_model()


class UserCreateView(CreateAPIView):
    
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [AllowAny]


class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    permission_classes = [AllowAny,]


class MeInfoView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = [IsAuthenticated,]

    def get(self, *args, **kwargs):
        user = self.request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
