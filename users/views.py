from users.filters import CustomUserFilter, ImageFilter
from rest_framework.viewsets import ModelViewSet
from users.serializers import (
    CustomUserCreateSerializer,
    CustomUserSerializer,
    ProfileImageSerializer,
)
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django_filters import rest_framework as filters
from users.models import CustomUser, ProfileImage
from rest_framework.permissions import IsAuthenticated


class CustomUserViewSet(ReadOnlyModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CustomUserFilter

    def get_serializer_class(self):
        if self.action == "create":
            return CustomUserCreateSerializer
        return CustomUserSerializer


class ProfileImageViewSet(ModelViewSet):
    queryset = ProfileImage.objects.all()
    serializer_class = ProfileImageSerializer

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ImageFilter
