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
    teachers_data ={
        'username': 'ademic',
        'first_name': 'michael',
        'last_name': 'ademic',
        'sex': CustomUser.SexChoices.MALE,
        'role': CustomUser.RoleChoices.TEACHER,
        'password': '12345678QQ',
        'date_of_birth': timezone.now().date()
    }
    
    response = client.post("/auth/users/", teachers_data)
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
    teachers_token = response.data["auth_token"]


    """ Student Login credentials """
    student_data ={
        'username': 'jenny',
        'first_name': 'jenny',
        'last_name': 'lane',
        'sex': CustomUser.SexChoices.FEMALE,
        'role': CustomUser.RoleChoices.STUDENT,
        'password': '12345678QQ',
        'date_of_birth': timezone.now().date()
    }
    """ Register Student """
    response = client.post("/auth/users/", student_data)
    assert response.status_code == 201
    assert response.data['username'] == 'jenny'

    """ Login Student """
    student_login_data = {
        "username": "jenny",
        "password": "12345678QQ",
    }
    response = client.post("/auth/login/", student_login_data)
    assert response.status_code == 200
    assert "auth_token" in response.data
    student_token = response.data["auth_token"]

    """ Admin Login credentials """
    admin_data ={
        'username': 'jeremy',
        'first_name': 'jeremy',
        'last_name': 'lane',
        'sex': CustomUser.SexChoices.MALE,
        'role': CustomUser.RoleChoices.ADMIN,
        'password': '12345678QQ',
        'date_of_birth': timezone.now().date()
    }
    """ Register admin """
    response = client.post("/auth/users/", admin_data)
    assert response.status_code == 201
    assert response.data['username'] == 'jeremy'

    """ Login admin """
    admin_login_data = {
        "username": "jeremy",
        "password": "12345678QQ",
    }
    response = client.post("/auth/login/", admin_login_data)
    assert response.status_code == 200
    assert "auth_token" in response.data
    admin_token = response.data["auth_token"]


    return {
        'client': client,
        'teacher_token': teachers_token,
        'student_token':student_token,
        'admin_token':admin_token

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
