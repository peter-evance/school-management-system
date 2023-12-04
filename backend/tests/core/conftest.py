from django.utils import timezone
import pytest
from core.models.classroom import ClassRoom
from core.choices import *
from users.models import CustomUser
from rest_framework.test import APIClient


@pytest.fixture
@pytest.mark.django_db
def setup_users():
    client = APIClient()
    registration_data ={
        'username': 'ademic',
        'first_name': 'michael',
        'last_name': 'ademic',
        'sex': CustomUser.SexChoices.MALE,
        'role': CustomUser.RoleChoices.TEACHER,
        'password': '12345678QQ',
        'date_of_birth': timezone.now().date()
    }
    
    response = client.post("/auth/users/", registration_data)
    assert response.status_code == 201
    assert response.data['username'] == 'ademic'


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
        "/authusers/me", HTTP_AUTHORIZATION=f"Token {token}",follow=True
    )

    return {
        'client': client,
        'token': token
    }

@pytest.fixture
def setup_subject_data():
    subject_data = {
        'title': 'English',
        'code': 'ENG',
        'added_at': timezone.now().date()
    }
    return subject_data


@pytest.fixture
def setup_classroom_data():
    classroom_data = {
        'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_2,
        'code': '',
        'capacity': 100,
        'stream': ClassRoomStreamChoices.B
    }
    return classroom_data
