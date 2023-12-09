from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from users.serializers import CustomUserCreateSerializer, CustomUserSerializer

from users.models import CustomUser


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CustomUserCreateSerializer
        return CustomUserSerializer
