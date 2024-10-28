from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.serializers import UserSerialize, UserSerializer


# Create your views here.


class CreateUserApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerialize


class UserListApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GetCurUserApiView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


    def get_object(self):
        print(self.request.user)
        return self.request.user

    lookup_url_kwarg = None
    lookup_field = None
