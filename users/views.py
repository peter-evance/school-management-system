from django.shortcuts import render
from users.filters import CustomUserFilter
from rest_framework.viewsets import ModelViewSet
from users.serializers import (
    CustomUserCreateSerializer,
    CustomUserSerializer,
    ProfileImageSerializer,
)
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from users.models import CustomUser, ProfileImage


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter

    def get_serializer_class(self):
        if self.action == "create":
            return CustomUserCreateSerializer
        return CustomUserSerializer


class ProfileImageViewSet(ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer
