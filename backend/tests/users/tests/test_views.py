from django.http import HttpResponse
import pytest
from rest_framework import status

from rest_framework.test import APIClient

from users.models import CustomUser

client = APIClient()

@pytest.mark.django_db
def test_user_registration(client):
    registration_data ={
        'username': 'ademic',
        'first_name': 'michael',
        'last_name': 'ademic',
        'sex': CustomUser.SexChoices.MALE,
        'role': CustomUser.RoleChoices.ADMIN,
        'password': '12345678QQ'
    }
    
    response = client.post("/auth/users/", registration_data)
    assert response.status_code == 201
    assert response.data['username'] == 'ademic'
    print(response.data)


    """user login test"""
    user_login_data = {
        "username": "ademic",
        "password": "12345678QQ",
    }
    response = client.post("/auth/login/", user_login_data)
    assert response.status_code == 200
    assert "auth_token" in response.data
    token = response.data["auth_token"]
    print(response.data)
    print(token)

    """Affirm user authorization"""
    response = client.get(
        "/authusers/me", HTTP_AUTHORIZATION=f"Token {token}",follow=True
    )
    assert response.status_code == 200
    assert "username" in response.data
    assert response.data["username"] == "ademic"
    assert response.data["role"] == "Admin"

    """Log out"""
    response = client.post(
        "/auth/logout/",
        HTTP_AUTHORIZATION=f"Token {token}",
    )
    assert response.status_code == 204

    