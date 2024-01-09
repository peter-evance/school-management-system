import os
import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from core.models.student import Student
from school_management_system.settings import BASE_DIR
from users.models import CustomUser

client = APIClient()


@pytest.mark.django_db
def test_user_registration(client):
    registration_data = {
        "username": "ademic",
        "first_name": "michael",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "date_of_birth": timezone.now().date(),
    }

    response = client.post("/auth/users/", registration_data)
    assert response.status_code == 201
    assert response.data["username"] == "ademic"
    assert Student.objects.all().exists()

    """user login test"""
    user_login_data = {
        "username": "ademic",
        "password": "12345678QQ",
    }
    response = client.post("/auth/login/", user_login_data)
    assert response.status_code == 200
    assert "auth_token" in response.data
    token = response.data["auth_token"]

    """Affirm user authorization"""
    response = client.get(
        "/authusers/me", HTTP_AUTHORIZATION=f"Token {token}", follow=True
    )
    assert response.status_code == 200
    assert "username" in response.data
    assert response.data["username"] == "ademic"
    assert response.data["role"] == "Student"

    """Log out"""
    response = client.post(
        "/auth/logout/",
        HTTP_AUTHORIZATION=f"Token {token}",
    )
    assert response.status_code == 204


@pytest.mark.django_db
def test_profile_image_upload(client):
    # Create a user for testin
    user_data = {
        "username": "ademic",
        "first_name": "michael",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "date_of_birth": timezone.now().date(),
    }
    response = client.post("/auth/users/", user_data)
    assert response.status_code == 201

    user = CustomUser.objects.get(username="ademic")

    image_path = os.path.join(BASE_DIR, "fixtures", "example.jpg")
    with open(image_path, "rb") as file:
        image_content = file.read()

    image_file = SimpleUploadedFile(
        "sample_image.jpg", image_content, content_type="image/jpg"
    )

    # Prepare data for profile image upload
    profile_image_data = {
        "user": user.id,
        "image": image_file,
    }
    response = client.post(
        reverse("users:profile-image-list"), profile_image_data, format="multipart"
    )
    response2 = client.post(
        reverse("users:profile-image-list"), profile_image_data, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    # print(response.data)
