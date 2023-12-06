from rest_framework import status
from django.utils import timezone
import pytest
from core.models.classroom import ClassRoom
from core.choices import *
from users.models import CustomUser
from rest_framework.test import APIClient

def generate_user_data(role: str,username: str) -> (dict[str, any] | None):
    role = role.lower()
    user_roles = {
        'teacher': CustomUser.RoleChoices.TEACHER,
        'admin': CustomUser.RoleChoices.ADMIN,
        'student': CustomUser.RoleChoices.STUDENT,
    }
    user_role = user_roles.get(role)
    if user_role is None:
        return None
    
    user_data = {
        'username': username,
        'first_name': 'michael',
        'last_name': 'ademic',
        'sex': CustomUser.SexChoices.MALE,
        'role': user_role,
        'password': '12345678QQ',
        'date_of_birth': timezone.now().date()
    }
    return user_data


@pytest.fixture
@pytest.mark.django_db
def setup_users():
    client = APIClient()
    role = 'teacher'
    username = 'ademic'
    teacher = generate_user_data(role, username)
    if not teacher:
        print(f'Invalid User role: {teacher.role}')
        return

    response = client.post("/auth/users/", teacher)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['username'] == username
    assert response.data['role'] == role.capitalize()


    """teacher login test"""
    user_login_data = {
        "username": username,
        "password": teacher['password'],
    }
    response = client.post("/auth/login/", user_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    teachers_token = response.data["auth_token"]


    """ Student Login credentials """
    role = 'student'
    std_username = 'john'
    student = generate_user_data(role, std_username)
    if not student:
        print(f'Invalid User role: {student.role}')
        return
    """ Register Student """
    response = client.post("/auth/users/", student)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['username'] == std_username

    """ Login Student """
    student_login_data = {
        "username": std_username,
        "password": student['password'],
    }
    response = client.post("/auth/login/", student_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    student_token = response.data["auth_token"]

    """ Admin Login credentials """
    role = 'admin'
    adm_username = 'jeremiah'
    admin = generate_user_data(role,adm_username)
    if not admin:
        print(f'Invalid User role: {admin.role}')
        return
    """ Register admin """
    response = client.post("/auth/users/", admin)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['username'] == adm_username

    """ Login admin """
    admin_login_data = {
       "username": adm_username,
        "password": admin['password'],
    }
    response = client.post("/auth/login/", admin_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    admin_token = response.data["auth_token"]


    return {
        'client': client,
        'teacher_token': teachers_token,
        'student_token':student_token,
        'admin_token':admin_token

    }


@pytest.fixture
def setup_test_data():
    subject_data = {
        'title': 'English',
        'code': 'ENG',
        'added_at': timezone.now().date()
    }
    classroom_data = {
        'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_2,
        'code': '',
        'capacity': 100,
        'stream': ClassRoomStreamChoices.B
    }
    
    return {
        'subject_data':subject_data,
        'classroom_data':classroom_data,
    }