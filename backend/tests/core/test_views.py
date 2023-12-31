from datetime import timedelta
import pytest
from core.choices import *
from core.serializers import *
from core.models.student import Student
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
class TestSubjectViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_subject_data):
        self.client = setup_users["client"]
        self.client = setup_users["client"]
        self.tokens = {
            "admin": setup_users["admin_token"],
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
        }
        self.subject_data = setup_subject_data["subject_data"]
        self.subject_data_obj = setup_subject_data["subject_data_obj"]

    def create_and_save(self):
        """This method serializes and save classroom object"""
        serializer = SubjectSerializer(data=self.subject_data)
        assert serializer.is_valid(), serializer.errors
        subject = serializer.save()
        return subject

    # """ ADD SUBJECTS (POST)"""
    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_201_CREATED),
            ("teacher", status.HTTP_201_CREATED),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_create_subject(self, user_type, expected_status):
        response = self.client.post(
            reverse("core:subjects-list"),
            data=self.subject_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_create_subject_with_no_authorizarion_unauthorized(self):
        """This returns unauthorised user 401"""
        response = self.client.post(
            reverse("core:subjects-list"), self.subject_data, format="json"
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not Subject.objects.filter(title=self.subject_data["title"])

    """ RETRIEVE SUBJECT (GET)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            # ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_view_subject(self, user_type, expected_status):
        Subject.objects.create(**self.subject_data_obj)
        response = self.client.get(
            reverse("core:subjects-list"),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_view_subject_with_no_authorizarion_unauthorized(self):
        """This returns unauthorised user 401"""
        response = self.client.get(
            reverse("core:subjects-list"),
            self.subject_data_obj,
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    """ RETRIEVE SUBJECT DETAILS (GET)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            # ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_view_subject_details(self, user_type, expected_status):
        subject = self.create_and_save()

        response = self.client.get(
            reverse("core:subjects-detail", kwargs={"pk": subject.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_view_subject_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        subject = self.create_and_save()
        response = self.client.get(
            reverse("core:subjects-detail", kwargs={"pk": subject.pk})
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    """ UPDATE SUBJECT (PATCH)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_subject(self, user_type, expected_status):
        subject = self.create_and_save()
        update_data = {
            "title": SubjectTitleChoices.CIVIC_EDUCATION,
            "code": SubjectCodeChoices.CVE,
        }

        response = self.client.patch(
            reverse("core:subjects-detail", kwargs={"pk": subject.id}),
            data=update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_update_subject_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        subject = self.create_and_save()
        data = {
            "title": SubjectTitleChoices.CIVIC_EDUCATION,
            "code": SubjectCodeChoices.CVE,
        }
        response = self.client.patch(
            reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
            data=data,
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Subject.objects.get(pk=subject.pk).code != SubjectCodeChoices.CVE

    """ DELETE SUBJECT (DELETE)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_204_NO_CONTENT),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_subject(self, user_type, expected_status):
        subject = self.create_and_save()

        response = self.client.delete(
            reverse("core:subjects-detail", kwargs={"pk": subject.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_delete_subject_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        subject = self.create_and_save()

        response = self.client.delete(
            reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Subject.objects.filter(pk=subject.pk).exists()

    """ FILTER SUBJECT (FILTER)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            # ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_filter_subjects_by_classroom(self, user_type, expected_status):
        self.create_and_save()
        filter_query = "?class_room=1"
        url = f"{reverse('core:subjects-list')}{filter_query}"

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_filter_subjects_by_classroom_without_authorization(self):
        self.create_and_save()
        filter_query = "?class_room=1"
        url = f"{reverse('core:subjects-list')}{filter_query}"
        response = self.client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


""" TEST CLASSROOM VIEWSET """


@pytest.mark.django_db
class TestClassRoomViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_classroom_data):
        self.client = setup_users["client"]
        self.tokens = {
            "admin": setup_users["admin_token"],
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
        }
        self.classroom_data = setup_classroom_data

    def create_and_save(self):
        """This method serializes and save classroom object"""
        serializer = ClassRoomSerializer(data=self.classroom_data)
        assert serializer.is_valid(), serializer.errors
        classroom = serializer.save()
        return classroom

    """ ADD CLASSROOM (POST)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_201_CREATED),
            ("teacher", status.HTTP_201_CREATED),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_create_classroom(self, user_type, expected_status):
        response = self.client.post(
            reverse("core:classrooms-list"),
            data=self.classroom_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_create_classroom_with_no_authorization(self):
        """This returns unauthorised user 401"""
        response = self.client.post(
            reverse("core:classrooms-list"), self.classroom_data, format="json"
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert not ClassRoom.objects.filter(title=self.classroom_data["code"])

    """ RETRIEVE SUBJECT (GET)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_view_classroom(self, user_type, expected_status):
        ClassRoom.objects.create(**self.classroom_data)
        response = self.client.get(
            reverse("core:classrooms-list"),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_view_classroom_with_no_authorizarion_unauthorized(self):
        """This returns unauthorised user 401"""
        response = self.client.get(
            reverse("core:classrooms-list"),
            self.classroom_data,
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    """ RETRIEVE CLASSROOM DETAILS (GET)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_view_classroom_details(self, user_type, expected_status):
        classroom = self.create_and_save()

        response = self.client.get(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_view_classroom_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        classroom = self.create_and_save()
        response = self.client.get(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.pk})
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    """ UPDATE CLASSROOM (PATCH)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_classroom_details(self, user_type, expected_status):
        classroom = self.create_and_save()
        update_data = {
            "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
            "code": ClassRoomCodeChoices.SSS_3,
        }

        response = self.client.patch(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.id}),
            data=update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_update_classroom_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        classroom = self.create_and_save()
        data = {
            "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
            "code": ClassRoomCodeChoices.SSS_3,
        }
        response = self.client.patch(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
            data=data,
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert ClassRoom.objects.get(pk=classroom.pk).title != data["title"]
        assert ClassRoom.objects.get(pk=classroom.pk).code != data["code"]

    """ DELETE CLASSROOM (DELETE)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_204_NO_CONTENT),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_classroom_details(self, user_type, expected_status):
        classroom = self.create_and_save()

        response = self.client.delete(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_delete_classroom_details_without_authorizarion(self):
        """This returns unauthorised user 401"""
        classroom = self.create_and_save()
        response = self.client.delete(
            reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert ClassRoom.objects.filter(pk=classroom.pk).exists()


""" TEST StudentViewSet """


@pytest.mark.django_db
class TestStudentViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_student_profile_data):
        self.client = setup_users["client"]
        self.tokens = {
            "admin": setup_users["admin_token"],
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
        }
        self.classroom = setup_student_profile_data["classroom"]
        self.enrolled_subjects = setup_student_profile_data["enrolled_subjects"]

    """ UPDATE STUDENTS (PATCH)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_student_profile(self, user_type, expected_status):
        student = Student.objects.get(id=1)
        update_data = {
            "classroom": self.classroom.pk,
            "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
        }

        response = self.client.patch(
            reverse("core:students-detail", kwargs={"pk": student.id}),
            data=update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )

        assert response.status_code == expected_status

    def test_update_student_profile_without_authorization(self):
        student = Student.objects.get(id=1)
        data = {
            "classroom": self.classroom.pk,
            "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
        }
        response = self.client.patch(
            reverse("core:students-detail", kwargs={"pk": student.pk}),
            data=data,
            format="json",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        updated_student = Student.objects.get(id=student.id)
        assert updated_student.classroom != self.classroom
        assert set(updated_student.enrolled_subjects.all()) != set(
            self.enrolled_subjects
        )

    """ DELETE STUDENTS_PROFILE (DELETE) """

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_204_NO_CONTENT),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_student_profile(self, user_type, expected_status):
        student = Student.objects.get(id=1)

        response = self.client.delete(
            reverse("core:students-detail", kwargs={"pk": student.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_delete_student_profile_without_authorization(self):
        """
        Test method to verify that a delete request without proper authorization results in an unauthorized response.

        Steps:
        1. Retrieve a student instance using the Student model.
        2. Send a DELETE request to the students-detail endpoint without proper authorization.
        3. Assert that the response status code is HTTP 401 UNAUTHORIZED.

        Notes:
        - The test ensures that a delete request without proper authorization is rejected.
        - The absence of authorization is simulated by not providing any authentication token.

        """
        student = Student.objects.get(id=1)

        response = self.client.delete(
            reverse("core:students-detail", kwargs={"pk": student.pk}),
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Student.objects.filter(id=student.pk).exists()

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            # ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_filter_students_by_name(self, user_type, expected_status):
        filter_query = "?name=lane"
        url = f"{reverse('core:students-list')}{filter_query}"

        response = self.client.get(
            url,
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_filter_students_by_classroom_without_authorization(self):
        Student.objects.get(id=1)
        filter_query = "?name=1"
        url = f"{reverse('core:students-list')}{filter_query}"
        response = self.client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED


""" TEST TeachersViewSet """


@pytest.mark.django_db
class TestTeacherViewSet:
    """
    Test suite class for the StudentViewSet API endpoints.

    This class includes tests for updating student profiles as a teacher.

    Attributes:
        client (APIClient): An instance of the Django REST Framework APIClient for making API requests.
        teachers_token (str): Authentication token for the teacher user.
        student_token (str): Authentication token for the student user.
        admin_token (str): Authentication token for the admin user.

    Note:
        This class assumes the existence of the Student model and appropriate API endpoints.
        The `setup_users` fixture is used to set up authentication tokens, and a student user
        (including the associated Student model) is created during the setup process.
    """

    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_student_profile_data):
        self.client = setup_users["client"]
        self.tokens = {
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
            "admin": setup_users["admin_token"],
        }
        self.classroom = setup_student_profile_data["classroom"]
        self.assigned_subjects = setup_student_profile_data["enrolled_subjects"]

    """ UPDATE TEACHER (PATCH)"""

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_403_FORBIDDEN),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_teacher_profile(self, user_type, expected_status):
        teacher = Teacher.objects.get(id=1)
        update_data = {
            "classroom": self.classroom.id,
            "assigned_subjects": [subject.id for subject in self.assigned_subjects],
        }

        response = self.client.patch(
            reverse("core:teachers-detail", kwargs={"pk": teacher.id}),
            data=update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )

        assert response.status_code == expected_status

    def test_update_teacher_profile_without_authorization(self):
        teacher = Teacher.objects.get(id=1)
        data = {
            "classroom": self.classroom.pk,
            "assigned_subjects": [subject.pk for subject in self.assigned_subjects],
        }
        response = self.client.patch(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            data=data,
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        updated_teacher = Teacher.objects.get(id=teacher.id)
        assert updated_teacher.classroom != self.classroom
        assert set(updated_teacher.assigned_subjects.all()) != set(
            self.assigned_subjects
        )

    """ DELETE TEACHER_PROFILE (DELETE) """

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_403_FORBIDDEN),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_teacher_profile(self, user_type, expected_status):
        teacher = Teacher.objects.get(id=1)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    def test_delete_teacher_profile_without_authorization(self):
        teacher = Teacher.objects.get(id=1)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Teacher.objects.filter(id=teacher.pk).exists()


@pytest.mark.django_db
class TestExamViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_exam_data):
        self.client = setup_users["client"]
        self.tokens = {
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
            "admin": setup_users["admin_token"],
        }

        self.exam_data = setup_exam_data

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_201_CREATED),
            ("teacher", status.HTTP_201_CREATED),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_create_exam(self, user_type, expected_status):
        response = self.client.post(
            reverse("core:exams-list"),
            data=self.exam_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_retrieve_exam(self, user_type, expected_status):
        response = self.client.get(
            reverse("core:exams-list"),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_exam(self, user_type, expected_status):
        serializer = ExamSerializer(data=self.exam_data)
        assert serializer.is_valid()
        exam_record = serializer.save()

        exam_update_data = {"duration": timedelta(hours=3)}

        response = self.client.patch(
            reverse("core:exams-detail", kwargs={"pk": exam_record.id}),
            data=exam_update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_204_NO_CONTENT),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_exam(self, user_type, expected_status):
        serializer = ExamSerializer(data=self.exam_data)
        assert serializer.is_valid()
        exam_record = serializer.save()

        exam_update_data = {"duration": timedelta(hours=3)}

        response = self.client.delete(
            reverse("core:exams-detail", kwargs={"pk": exam_record.id}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status
        print(response.data)


@pytest.mark.django_db
class TestSubjectResultViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_exam_result_data):
        self.client = setup_users["client"]
        self.tokens = {
            "admin": setup_users["admin_token"],
            "teacher": setup_users["teacher_token"],
            "student": setup_users["student_token"],
        }
        self.result_data = setup_exam_result_data

    def create_and_save(self):
        """This method serializes and save classroom object"""
        serializer = SubjectResultSerializer(data=self.result_data)
        assert serializer.is_valid(), serializer.errors
        subject = serializer.save()
        return subject

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_201_CREATED),
            ("teacher", status.HTTP_201_CREATED),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_create_student_result(self, user_type, expected_status):
        response = self.client.post(
            reverse("core:subject-results-list"),
            data=self.result_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_retrieve_student_result(self, user_type, expected_status):
        response = self.client.get(
            reverse("core:subject-results-list"),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_200_OK),
            ("teacher", status.HTTP_200_OK),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_update_student_result(self, user_type, expected_status):
        student_result_data = self.create_and_save()

        result_update_data = {"duration": timedelta(hours=3)}

        response = self.client.patch(
            reverse(
                "core:subject-results-detail", kwargs={"pk": student_result_data.id}
            ),
            data=result_update_data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status

    @pytest.mark.parametrize(
        "user_type, expected_status",
        [
            ("admin", status.HTTP_204_NO_CONTENT),
            ("teacher", status.HTTP_204_NO_CONTENT),
            ("student", status.HTTP_403_FORBIDDEN),
        ],
    )
    def test_delete_student_result(self, user_type, expected_status):
        student_result_data = self.create_and_save()

        response = self.client.delete(
            reverse(
                "core:subject-results-detail", kwargs={"pk": student_result_data.id}
            ),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.tokens[user_type]}",
        )
        assert response.status_code == expected_status
        print(response.data)
