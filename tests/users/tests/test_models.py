import pytest

from users.serializers import CustomUserCreateSerializer


class TestCreateUser:
    @pytest.mark.django_db
    def test_create_user(self):
        serializer = CustomUserCreateSerializer(
            data={
                "username": "michaelademic",
                "first_name": "michael",
                "last_name": "ademic",
                "sex": "Male",
                "role": "Teacher",
                "password": "12345678QQ",
                "re_password": "12345678QQ",
            }
        )

        if serializer.is_valid():
            user = serializer.save()
