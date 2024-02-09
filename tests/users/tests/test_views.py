import os
import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient
from django.core import mail
from django.core.files.uploadedfile import SimpleUploadedFile
from core.models.student import Student
from school_management_system.settings import BASE_DIR
from users.models import CustomUser

client = APIClient()


@pytest.fixture
def registration_data():
    return {
        "username": "ademic",
        "first_name": "michael",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example@gmail.com",
        "date_of_birth": timezone.now().date(),
    }


@pytest.mark.django_db
def test_user_registration(client, registration_data):
    response = client.post("/auth/users/", registration_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["username"] == "ademic"
    assert Student.objects.all().exists()

    # Check that the user is not active
    user = CustomUser.objects.get(username="ademic")
    assert not user.is_active

    # Bypass Djoser User Activation
    user = CustomUser.objects.get(email="example@gmail.com")
    user.is_active = True
    user.save()

    # Assert an email is sent
    email_object = mail.outbox[0]
    assert email_object.subject == "Account activation on The Gem"
    assert email_object.to == ["example@gmail.com"]

    # User login test
    user_login_data = {"email": "example@gmail.com", "password": "12345678QQ"}
    response = client.post("/users/login/", user_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data


@pytest.mark.django_db
def test_profile_image_upload(client, registration_data):
    response = client.post("/auth/users/", registration_data)
    assert response.status_code == status.HTTP_201_CREATED

    user = CustomUser.objects.get(username="ademic")

    image_path = os.path.join(BASE_DIR, "fixtures", "example.jpg")
    with open(image_path, "rb") as file:
        image_content = file.read()

    image_file = SimpleUploadedFile(
        "sample_image.jpg", image_content, content_type="image/jpg"
    )

    # Prepare data for profile image upload
    profile_image_data = {"user": user.id, "image": image_file}
    response = client.post(
        "/users/profile-images/", profile_image_data, format="multipart"
    )
    response2 = client.post(
        "/users/profile-images/", profile_image_data, format="multipart"
    )

    assert response.status_code == status.HTTP_201_CREATED
    print(response.data)


@pytest.mark.django_db
def test_user_approval(client, registration_data):
    # Create registration data for two users
    registration_data1 = registration_data.copy()
    registration_data1.update(
        {
            "username": "ademic",
            "role": CustomUser.RoleChoices.ADMIN,
            "email": "example@gmail.com",
        }
    )

    registration_data2 = registration_data.copy()
    registration_data2.update(
        {
            "username": "peterson",
            "role": CustomUser.RoleChoices.STUDENT,
            "email": "example1@gmail.com",
        }
    )

    # Create two users
    response1 = client.post("/auth/users/", registration_data1)
    response2 = client.post("/auth/users/", registration_data2)

    # Assert successful creation of users
    assert response1.status_code == status.HTTP_201_CREATED
    assert response2.status_code == status.HTTP_201_CREATED

    # Ensure users are created
    assert CustomUser.objects.all().exists()

    # Approve the newly created users who is not admin
    user1 = CustomUser.objects.get(username="ademic")
    user2 = CustomUser.objects.get(username="peterson")
    user1.is_active = True
    user2.is_active = True
    user1.save()
    user2.save()

    # Login as user1 to get authentication token
    user_login_data = {"email": "example@gmail.com", "password": "12345678QQ"}
    response = client.post("/users/login/", user_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    token = response.data["auth_token"]

    # PATCH request to approve user2
    data = {"user_ids": [user2.id]}
    response = client.patch(
        "/users/profiles/approve_new_users/",
        data,
        HTTP_AUTHORIZATION=f"Token {token}",
        content_type="application/json",
    )

    # Assert the PATCH request is successful
    assert response.status_code == status.HTTP_200_OK

    # Refresh user2 instance from the database
    user2.refresh_from_db()

    # Assert user2 is approved
    assert user2.is_approved

    # Assert an email is sent
    email_object = mail.outbox[2]
    assert len(mail.outbox) == 3
    assert email_object.subject == "Your account has been approved"
    assert email_object.to == ["example1@gmail.com"]
