from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework.serializers import (
    ModelSerializer,
)

from users.models import CustomUser, ProfileImage


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password",
            "sex",
            "first_name",
            "last_name",
            "role",
            "date_of_birth",
            "address",
            "email",
        )


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "sex",
            "date_of_birth",
            "address",
            "email",
            "role",
            "is_active",
        )

class CustomUserSerializer2(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "sex",
            "date_of_birth",
            "address",
            "email",
            "role",
        )


class ProfileImageSerializer(ModelSerializer):
    class Meta:
        model = ProfileImage
        fields = ["user", "image", "thumbnail"]
