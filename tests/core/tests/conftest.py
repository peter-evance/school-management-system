from datetime import timedelta
from rest_framework import status
from django.utils import timezone
import pytest
from core.models.exams import Exam
from core.serializers import ClassRoomSerializer, ExamSerializer, SubjectSerializer
from users.serializers import CustomUserCreateSerializer
from core.models.classroom import ClassRoom
from core.choices import *
from users.models import CustomUser
from rest_framework.test import APIClient


@pytest.fixture
@pytest.mark.django_db
def setup_users():
    """
    Fixture to set up and authenticate users for testing.

    Returns:
        dict: A dictionary containing client and authentication tokens for teacher, student, and admin.
            Keys:
            - 'client': APIClient instance for making API requests.
            - 'teacher_token': Authentication token for the teacher user.
            - 'student_token': Authentication token for the student user.
            - 'admin_token': Authentication token for the admin user.
    """
    client = APIClient()

    # Teacher user data
    teacher_data = {
        "username": "toughest_teacher",
        "role": CustomUser.RoleChoices.TEACHER,
        "first_name": "Michael1",
        "last_name": "Ademic",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=500),
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example@gmail.com",
    }

    # Create teacher user
    response = client.post("/auth/users/", teacher_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["username"] == teacher_data["username"]

    # Check that the user is not active
    user = CustomUser.objects.get(email="example@gmail.com")
    assert not user.is_active

    # Bypass Djoser User Activation
    user = CustomUser.objects.get(email="example@gmail.com")
    user.is_active = True
    user.save()

    # Teacher login
    teacher_login_data = {
        "email": teacher_data["email"],
        "password": teacher_data["password"],
    }
    response = client.post("/users/login/", teacher_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    teachers_token = response.data["auth_token"]

    # Student user data
    student_data = {
        "username": "toughest_student",
        "role": CustomUser.RoleChoices.STUDENT,
        "first_name": "Michael2",
        "last_name": "Ademic",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=50),
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example1@gmail.com",
    }

    # Create student user
    response = client.post("/auth/users/", student_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["username"] == student_data["username"]

    # Check that the user is not active
    user = CustomUser.objects.get(email="example1@gmail.com")
    assert not user.is_active

    # Bypass Djoser User Activation
    user = CustomUser.objects.get(email="example1@gmail.com")
    user.is_active = True
    user.save()

    # Student login
    student_login_data = {
        "email": student_data["email"],
        "password": student_data["password"],
    }
    response = client.post("/users/login/", student_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    student_token = response.data["auth_token"]

    # Admin user data
    admin_data = {
        "username": "toughest_admin",
        "role": CustomUser.RoleChoices.ADMIN,
        "first_name": "Michael3",
        "last_name": "Ademic",
        "sex": CustomUser.SexChoices.MALE,
        "date_of_birth": timezone.now().date() - timedelta(weeks=1000),
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example2@gmail.com",
    }

    # Create admin user
    response = client.post("/auth/users/", admin_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data["username"] == admin_data["username"]

    # Check that the user is not active
    user = CustomUser.objects.get(email="example2@gmail.com")
    assert not user.is_active

    # Bypass Djoser User Activation
    user = CustomUser.objects.get(email="example2@gmail.com")
    user.is_active = True
    user.save()

    # Admin login
    admin_login_data = {
        "email": admin_data["email"],
        "password": admin_data["password"],
    }
    response = client.post("/users/login/", admin_login_data)
    assert response.status_code == status.HTTP_200_OK
    assert "auth_token" in response.data
    admin_token = response.data["auth_token"]

    return {
        "client": client,
        "teacher_token": teachers_token,
        "student_token": student_token,
        "admin_token": admin_token,
    }


@pytest.fixture
def setup_subject_data():
    from core.serializers import ClassRoomSerializer, SubjectSerializer

    def create_and_save(serializer):
        assert serializer.is_valid()
        return serializer.save()

    classroom_data = {
        "title": ClassRoomTitleChoices.JUNIOR_SECONDARY_SCHOOL_3,
        "code": ClassRoomCodeChoices.JSS_3,
        "capacity": 200,
        "stream": "A",
    }
    classroom = create_and_save(ClassRoomSerializer(data=classroom_data))
    subject_data = {
        "title": SubjectTitleChoices.ENGLISH_LANGUAGE,
        "code": SubjectCodeChoices.ENG,
        "class_room": classroom.pk,
    }
    subject_data_obj = {
        "title": SubjectTitleChoices.ENGLISH_LANGUAGE,
        "code": SubjectCodeChoices.ENG,
        "class_room": classroom,
    }
    return {"subject_data": subject_data, "subject_data_obj": subject_data_obj}


@pytest.fixture()
def setup_student_data():
    student = {
        "username": "jane",
        "first_name": "lane",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example3@gmail.com",
        "date_of_birth": timezone.now().date() - timedelta(weeks=500),
    }
    return student


@pytest.fixture()
def setup_classroom_data():
    classroom = {
        "title": ClassRoomTitleChoices.JUNIOR_SECONDARY_SCHOOL_3,
        "code": ClassRoomCodeChoices.JSS_3,
        "capacity": 200,
        "stream": "A",
    }
    return classroom


@pytest.fixture
@pytest.mark.django_db
def setup_student_profile_data():
    from core.serializers import ClassRoomSerializer, SubjectSerializer
    from users.serializers import CustomUserCreateSerializer

    def create_and_save(serializer):
        assert serializer.is_valid()
        return serializer.save()

    student_data = {
        "username": "jane",
        "first_name": "lane",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example4@gmail.com",
        "date_of_birth": timezone.now().date(),
    }
    user = create_and_save(CustomUserCreateSerializer(data=student_data))

    classroom_data = {
        "title": ClassRoomTitleChoices.JUNIOR_SECONDARY_SCHOOL_3,
        "code": ClassRoomCodeChoices.JSS_3,
        "capacity": 200,
        "stream": "A",
    }
    classroom = create_and_save(ClassRoomSerializer(data=classroom_data))

    subjects_data = [
        {
            "title": SubjectTitleChoices.ENGLISH_LANGUAGE,
            "code": SubjectCodeChoices.ENG,
            "class_room": classroom.pk,
        },
        {
            "title": SubjectTitleChoices.MATHEMATICS,
            "code": SubjectCodeChoices.MTH,
            "class_room": classroom.pk,
        },
        {
            "title": SubjectTitleChoices.BIOLOGY,
            "code": SubjectCodeChoices.BIO,
            "class_room": classroom.pk,
        },
    ]
    enrolled_subjects = [
        create_and_save(SubjectSerializer(data=sub_data)) for sub_data in subjects_data
    ]

    student_profile_data = {
        "user": user.pk,
        "classroom": classroom.pk,
        "enrolled_subjects": [sub.pk for sub in enrolled_subjects],
    }
    return {
        "classroom": classroom,
        "enrolled_subjects": enrolled_subjects,
        "student_profile_data": student_profile_data,
    }


@pytest.fixture
def setup_exam_data():
    def create_and_save(serializer):
        assert serializer.is_valid()
        return serializer.save()

    classroom_data = {
        "title": ClassRoomTitleChoices.JUNIOR_SECONDARY_SCHOOL_3,
        "code": ClassRoomCodeChoices.JSS_3,
        "capacity": 200,
        "stream": "A",
    }

    classroom = create_and_save(ClassRoomSerializer(data=classroom_data))

    subject_data = {
        "title": SubjectTitleChoices.ENGLISH_LANGUAGE,
        "code": SubjectCodeChoices.ENG,
        "class_room": classroom.id,
    }
    subject = create_and_save(SubjectSerializer(data=subject_data))

    exam_data = {
        "exam_type": ExamType.FINAL,
        "subject": subject.id,
        "duration": timedelta(hours=2, minutes=30),
        "max_marks": 100,
    }

    return exam_data


@pytest.fixture
def setup_exam_result_data():
    def create_and_save(serializer):
        assert serializer.is_valid()
        return serializer.save()

    classroom_data = {
        "title": ClassRoomTitleChoices.JUNIOR_SECONDARY_SCHOOL_3,
        "code": ClassRoomCodeChoices.JSS_3,
        "capacity": 200,
        "stream": "A",
    }

    classroom = create_and_save(ClassRoomSerializer(data=classroom_data))

    subject_data = {
        "title": SubjectTitleChoices.ENGLISH_LANGUAGE,
        "code": SubjectCodeChoices.ENG,
        "class_room": classroom.id,
    }
    subject = create_and_save(SubjectSerializer(data=subject_data))

    exam = {
        "exam_type": ExamType.FINAL,
        "subject": subject.id,
        "duration": timedelta(hours=2, minutes=30),
        "max_marks": 100,
    }

    exam_data = create_and_save(ExamSerializer(data=exam))

    student_data = {
        "username": "jane",
        "first_name": "lane",
        "last_name": "ademic",
        "sex": CustomUser.SexChoices.MALE,
        "role": CustomUser.RoleChoices.STUDENT,
        "password": "12345678QQ",
        "re_password": "12345678QQ",
        "email": "example5@gmail.com",
        "date_of_birth": timezone.now().date(),
    }
    user = create_and_save(CustomUserCreateSerializer(data=student_data))

    result_data = {"student": 2, "exam": exam_data.id, "marks_obtained": 70}
    return result_data
