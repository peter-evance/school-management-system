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
        self.teachers_token = setup_users["teacher_token"]
        self.student_token = setup_users["student_token"]
        self.admin_token = setup_users["admin_token"]
        self.subject_data = setup_subject_data["subject_data"]
        self.subject_data_obj = setup_subject_data["subject_data_obj"]

    def create_and_save(self):
        """This method serializes and save classroom object"""
        serializer = SubjectSerializer(data=self.subject_data)
        assert serializer.is_valid(), serializer.errors
        subject = serializer.save()
        return subject

    # """ ADD SUBJECTS (POST)"""

    # def test_add_subject_as_a_teacher(self):
    #     response = self.client.post(
    #         reverse("core:subjects-list"),
    #         self.subject_data,
    #         format="json",
    #         HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
    #     )
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert Subject.objects.all()

    # def test_add_subject_as_an_admin(self):
    #     response = self.client.post(
    #         reverse("core:subjects-list"),
    #         self.subject_data,
    #         format="json",
    #         HTTP_AUTHORIZATION=f"Token {self.admin_token}",
    #     )
    #     assert response.status_code == status.HTTP_201_CREATED
    #     assert Subject.objects.all()

    # def test_add_subject_as_a_student_permission_denied(self):
    #     response = self.client.post(
    #         reverse("core:subjects-list"),
    #         self.subject_data,
    #         format="json",
    #         HTTP_AUTHORIZATION=f"Token {self.student_token}",
    #     )
    #     assert response.status_code == status.HTTP_403_FORBIDDEN

    # def test_add_subject_with_no_authorizarion_unauthorized(self):
    #     """This returns unauthorised user 401"""
    #     response = self.client.post(
    #         reverse("core:subjects-list"), self.subject_data, format="json"
    #     )
    #     print(response.data)
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED
    #     assert not Subject.objects.filter(title=self.subject_data["title"])

    # """ RETRIEVE SUBJECT (GET)"""

    # def test_view_subject_as_a_teacher(self):
    #     Subject.objects.create(**self.subject_data_obj)
    #     response = self.client.get(
    #         reverse("core:subjects-list"),
    #         HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
    #     )
    #     print(response.data)
    #     # assert response.status_code == status.HTTP_200_OK

    # def test_view_subject_as_an_admin(self):
    #     Subject.objects.create(**self.subject_data_obj)
    #     response = self.client.get(
    #         reverse("core:subjects-list"),
    #         HTTP_AUTHORIZATION=f"Token {self.admin_token}",
    #         follow=True,
    #     )
    #     assert response.status_code == status.HTTP_200_OK

    # def test_view_subject_as_a_student_permission_denied(self):
    #     Subject.objects.create(**self.subject_data_obj)
    #     response = self.client.get(
    #         reverse("core:subjects-list"),
    #         HTTP_AUTHORIZATION=f"Token {self.student_token}",
    #     )
    #     assert response.status_code == status.HTTP_403_FORBIDDEN

    # def test_view_subject_with_no_authorizarion_unauthorized(self):
    #     """This returns unauthorised user 401"""
    #     response = self.client.get(
    #         reverse("core:subjects-list"),
    #         self.subject_data_obj,
    #         format="json",
    #     )
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # """ RETRIEVE SUBJECT DETAILS (GET)"""

    # def test_view_subject_details_as_an_admin(self):
    #     subject = self.create_and_save()
    #     response = self.client.get(
    #         reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
    #         HTTP_AUTHORIZATION=f"Token {self.admin_token}",
    #     )
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["title"] == subject.title

    # def test_view_subject_details_as_a_teacher(self):
    #     subject = self.create_and_save()
    #     response = self.client.get(
    #         reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
    #         HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
    #     )
    #     assert response.status_code == status.HTTP_200_OK
    #     assert response.data["title"] == subject.title

    # def test_view_subject_details_as_a_student_permission_denied(self):
    #     subject = self.create_and_save()
    #     response = self.client.get(
    #         reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
    #         HTTP_AUTHORIZATION=f"Token {self.student_token}",
    #     )
    #     assert response.status_code == status.HTTP_403_FORBIDDEN

    # def test_view_subject_details_without_authorizarion(self):
    #     """This returns unauthorised user 401"""
    #     subject = self.create_and_save()
    #     response = self.client.get(
    #         reverse("core:subjects-detail", kwargs={"pk": subject.pk})
    #     )
    #     assert response.status_code == status.HTTP_401_UNAUTHORIZED


#     """ UPDATE SUBJECT (PATCH)"""

#     def test_update_subject_details_as_an_admin(self):
#         subject = self.create_and_save()
#         data = {"code": "GST"}
#         response = self.client.patch(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == subject.title
#         assert Subject.objects.get(pk=subject.pk).code == "GST"

#     def test_update_subject_details_as_a_teacher(self):
#         subject = self.create_and_save()
#         data = {"code": "GST"}
#         response = self.client.patch(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == subject.title
#         assert Subject.objects.get(pk=subject.pk).code == "GST"

#     def test_update_subject_details_as_a_student_permission_denied(self):
#         subject = self.create_and_save()
#         data = {"code": "GST"}
#         response = self.client.patch(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert Subject.objects.get(pk=subject.pk).code != "GST"

#     def test_update_subject_details_without_authorizarion(self):
#         """This returns unauthorised user 401"""
#         subject = self.create_and_save()
#         data = {"code": "GST"}
#         response = self.client.patch(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             data=data,
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert Subject.objects.get(pk=subject.pk).code != "GST"

#     """ DELETE SUBJECT (DELETE)"""

#     def test_delete_subject_details_as_an_admin(self):
#         subject = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_as_a_teacher(self):
#         subject = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_as_a_student_permission_denied(self):
#         subject = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_without_authorizarion(self):
#         """This returns unauthorised user 401"""
#         subject = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:subjects-detail", kwargs={"pk": subject.pk}),
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert Subject.objects.filter(pk=subject.pk).exists()


# """ TEST CLASSROOM VIEWSET """


# @pytest.mark.django_db
# class TestClassRoomViewSet:
#     @pytest.fixture(autouse=True)
#     def setup(self, setup_users, setup_classroom_data):
#         self.client = setup_users["client"]
#         self.teachers_token = setup_users["teacher_token"]
#         self.student_token = setup_users["student_token"]
#         self.admin_token = setup_users["admin_token"]
#         self.classroom_data = setup_classroom_data

#     def create_and_save(self):
#         """This method serializes and save classroom object"""
#         serializer = ClassRoomSerializer(data=self.classroom_data)
#         assert serializer.is_valid(), serializer.errors
#         classroom = serializer.save()
#         return classroom

#     """ ADD CLASSROOM (POST)"""

#     def test_add_classroom_as_a_teacher(self):
#         response = self.client.post(
#             reverse("core:classrooms-list"),
#             self.classroom_data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_201_CREATED
#         assert ClassRoom.objects.all()

#     def test_add_classroom_as_an_admin(self):
#         response = self.client.post(
#             reverse("core:classrooms-list"),
#             self.classroom_data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_201_CREATED
#         assert ClassRoom.objects.all()

#     def test_add_classroom_as_a_student_permission_denied(self):
#         response = self.client.post(
#             reverse("core:classrooms-list"),
#             self.classroom_data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_add_classroom_with_no_authorization(self):
#         """This returns unauthorised user 401"""
#         response = self.client.post(
#             reverse("core:classrooms-list"), self.classroom_data, format="json"
#         )
#         print(response.data)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert not ClassRoom.objects.filter(title=self.classroom_data["code"])

#     """ RETRIEVE SUBJECT (GET)"""

#     def test_view_classroom_as_a_teacher(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(
#             reverse("core:classrooms-list"),
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_classroom_as_an_admin(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(
#             reverse("core:classrooms-list"),
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#             follow=True,
#         )
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_classroom_as_a_student_permission_denied(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(
#             reverse("core:classrooms-list"),
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_view_classroom_with_no_authorizarion_unauthorized(self):
#         """This returns unauthorised user 401"""
#         response = self.client.get(
#             reverse("core:classrooms-list"),
#             self.classroom_data,
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ RETRIEVE CLASSROOM DETAILS (GET)"""

#     def test_view_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()
#         response = self.client.get(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == classroom.title

#     def test_view_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()
#         response = self.client.get(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == classroom.title

#     def test_view_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()
#         response = self.client.get(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_view_classroom_details_without_authorizarion(self):
#         """This returns unauthorised user 401"""
#         classroom = self.create_and_save()
#         response = self.client.get(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk})
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ UPDATE CLASSROOM (PATCH)"""

#     def test_update_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()
#         data = {
#             "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             "code": ClassRoomCodeChoices.SSS_3,
#         }
#         response = self.client.patch(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == data["title"]
#         assert ClassRoom.objects.get(pk=classroom.pk).code == data["code"]

#     def test_update_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()
#         data = {
#             "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             "code": ClassRoomCodeChoices.SSS_3,
#         }
#         response = self.client.patch(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data["title"] == data["title"]
#         assert ClassRoom.objects.get(pk=classroom.pk).code == data["code"]

#     def test_update_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()
#         data = {
#             "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             "code": ClassRoomCodeChoices.SSS_3,
#         }
#         response = self.client.patch(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert ClassRoom.objects.get(pk=classroom.pk).title != data["title"]
#         assert ClassRoom.objects.get(pk=classroom.pk).code != data["code"]

#     def test_update_classroom_details_without_authorizarion(self):
#         """This returns unauthorised user 401"""
#         classroom = self.create_and_save()
#         data = {
#             "title": ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             "code": ClassRoomCodeChoices.SSS_3,
#         }
#         response = self.client.patch(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             data=data,
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert ClassRoom.objects.get(pk=classroom.pk).title != data["title"]
#         assert ClassRoom.objects.get(pk=classroom.pk).code != data["code"]

#     """ DELETE CLASSROOM (DELETE)"""

#     def test_delete_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_without_authorizarion(self):
#         """This returns unauthorised user 401"""
#         classroom = self.create_and_save()
#         response = self.client.delete(
#             reverse("core:classrooms-detail", kwargs={"pk": classroom.pk}),
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert ClassRoom.objects.filter(pk=classroom.pk).exists()


# """ TEST StudentViewSet """


# @pytest.mark.django_db
# class TestStudentViewSet:
#     """
#     Test suite class for the StudentViewSet API endpoints.

#     This class includes tests for updating student profiles as a teacher.

#     Attributes:
#         client (APIClient): An instance of the Django REST Framework APIClient for making API requests.
#         teachers_token (str): Authentication token for the teacher user.
#         student_token (str): Authentication token for the student user.
#         admin_token (str): Authentication token for the admin user.

#     Note:
#         This class assumes the existence of the Student model and appropriate API endpoints.
#         The `setup_users` fixture is used to set up authentication tokens, and a student user
#         (including the associated Student model) is created during the setup process.
#     """

#     @pytest.fixture(autouse=True)
#     def setup(self, setup_users, setup_student_profile_data):
#         self.client = setup_users["client"]
#         self.teachers_token = setup_users["teacher_token"]
#         self.student_token = setup_users["student_token"]
#         self.admin_token = setup_users["admin_token"]
#         self.classroom = setup_student_profile_data["classroom"]
#         self.enrolled_subjects = setup_student_profile_data["enrolled_subjects"]

#     """ UPDATE STUDENTS (PATCH)"""

#     def test_update_student_profile_as_a_teacher(self):
#         """
#         Test method to check if a teacher can successfully update a student's profile.

#         Steps:
#         1. Retrieves a student instance using the Student model.
#         2. Prepares data for updating the student's profile (e.g., classroom, enrolled_subjects).
#         3. Sends a PATCH request to the students-detail endpoint with teacher authentication.
#         4. Asserts that the response status code is HTTP 200 OK.
#         5. Retrieve the updated student instance from the database.
#         6. Assert that the student's classroom has been updated as expected.
#         7. Assert that the enrolled subjects of the updated student match the expected subjects.
#         """
#         student = Student.objects.get(id=1)
#         data = {
#             "classroom": self.classroom.pk,
#             "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
#         }
#         response = self.client.patch(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_200_OK
#         updated_student = Student.objects.get(id=student.id)
#         assert updated_student.classroom == self.classroom
#         assert set(updated_student.enrolled_subjects.all()) == set(
#             self.enrolled_subjects
#         )

#     def test_update_student_profile_as_an_admin(self):
#         """
#         Test method to check if an admin can successfully update a student's profile.

#         Steps:
#         1. Retrieves a student instance using the Student model.
#         2. Prepares data for updating the student's profile (e.g., classroom, enrolled_subjects).
#         3. Sends a PATCH request to the students-detail endpoint with teacher authentication.
#         4. Asserts that the response status code is HTTP 200 OK.
#         5. Retrieve the updated student instance from the database.
#         6. Assert that the student's classroom has been updated as expected.
#         7. Assert that the enrolled subjects of the updated student match the expected subjects.
#         """
#         student = Student.objects.get(id=1)
#         data = {
#             "classroom": self.classroom.pk,
#             "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
#         }
#         response = self.client.patch(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )

#         assert response.status_code == status.HTTP_200_OK
#         updated_student = Student.objects.get(id=student.id)
#         assert updated_student.classroom == self.classroom
#         assert set(updated_student.enrolled_subjects.all()) == set(
#             self.enrolled_subjects
#         )

#     def test_update_student_profile_as_a_student_permission_denied(self):
#         student = Student.objects.get(id=1)
#         data = {
#             "classroom": self.classroom.pk,
#             "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
#         }
#         response = self.client.patch(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             data=data,
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )

#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         updated_student = Student.objects.get(id=student.id)
#         assert updated_student.classroom != self.classroom
#         assert set(updated_student.enrolled_subjects.all()) != set(
#             self.enrolled_subjects
#         )

#     def test_update_student_profile_without_authorization(self):
#         student = Student.objects.get(id=1)
#         data = {
#             "classroom": self.classroom.pk,
#             "enrolled_subjects": [subject.pk for subject in self.enrolled_subjects],
#         }
#         response = self.client.patch(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             data=data,
#             format="json",
#         )

#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         updated_student = Student.objects.get(id=student.id)
#         assert updated_student.classroom != self.classroom
#         assert set(updated_student.enrolled_subjects.all()) != set(
#             self.enrolled_subjects
#         )

#     """ DELETE STUDENTS_PROFILE (DELETE) """

#     def test_delete_student_profile_as_an_admin(self):
#         """
#         Test method to verify that an admin can successfully delete a student's profile.

#         Steps:
#         1. Retrieve a student instance using the Student model.
#         2. Send a DELETE request to the students-detail endpoint with admin authentication.
#         3. Assert that the response status code is HTTP 204 NO CONTENT.
#         4. Verify that the student instance is no longer present in the database.

#         Notes:
#         - The test ensures that an admin has the authority to delete a student's profile.
#         - The admin's authentication token is used to authenticate the DELETE request.

#         """
#         student = Student.objects.get(id=1)

#         response = self.client.delete(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.admin_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Student.objects.filter(id=student.pk).exists()

#     def test_delete_student_profile_a_teacher(self):
#         """
#         Test method to verify that a teacher can successfully delete a student's profile.

#         Steps:
#         1. Retrieve a student instance using the Student model.
#         2. Send a DELETE request to the students-detail endpoint with admin authentication.
#         3. Assert that the response status code is HTTP 204 NO CONTENT.
#         4. Verify that the student instance is no longer present in the database.

#         Notes:
#         - The test ensures that a teacher has the authority to delete a student's profile.
#         - The teacher's authentication token is used to authenticate the DELETE request.

#         """
#         student = Student.objects.get(id=1)

#         response = self.client.delete(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
#         )
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Student.objects.filter(id=student.pk).exists()

#     def test_delete_student_profile_a_student_permission_denied(self):
#         """
#         Test method to verify that a student cannot delete their own profile.

#         Steps:
#         1. Retrieve a student instance using the Student model.
#         2. Send a DELETE request to the students-detail endpoint with student authentication.
#         3. Assert that the response status code is HTTP 403 FORBIDDEN.
#         4. Assert that the student instance still exists in the database.

#         Notes:
#         - The test ensures that a student does not have permission to delete their own profile.
#         - The student's authentication token is used to authenticate the DELETE request.

#         """
#         student = Student.objects.get(id=1)

#         response = self.client.delete(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             format="json",
#             HTTP_AUTHORIZATION=f"Token {self.student_token}",
#         )
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert Student.objects.filter(id=student.pk).exists()

#     def test_delete_student_profile_without_authorization(self):
#         """
#         Test method to verify that a delete request without proper authorization results in an unauthorized response.

#         Steps:
#         1. Retrieve a student instance using the Student model.
#         2. Send a DELETE request to the students-detail endpoint without proper authorization.
#         3. Assert that the response status code is HTTP 401 UNAUTHORIZED.
#         4. Assert that the student instance still exists in the database.

#         Notes:
#         - The test ensures that a delete request without proper authorization is rejected.
#         - The absence of authorization is simulated by not providing any authentication token.

#         """
#         student = Student.objects.get(id=1)

#         response = self.client.delete(
#             reverse("core:students-detail", kwargs={"pk": student.pk}),
#             format="json",
#         )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert Student.objects.filter(id=student.pk).exists()


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
        self.teachers_token = setup_users["teacher_token"]
        self.student_token = setup_users["student_token"]
        self.admin_token = setup_users["admin_token"]
        self.classroom = setup_student_profile_data["classroom"]
        self.assigned_subjects = setup_student_profile_data["enrolled_subjects"]

    """ UPDATE TEACHER (PATCH)"""

    def test_update_teacher_profile_as_an_admin(self):
        teacher = Teacher.objects.get(id=1)
        data = {
            "classroom": self.classroom.pk,
            "assigned_subjects": [subject.pk for subject in self.assigned_subjects],
        }
        response = self.client.patch(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            data=data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.admin_token}",
        )

        assert response.status_code == status.HTTP_200_OK
        updated_teacher = Teacher.objects.get(id=teacher.id)
        assert updated_teacher.classroom == self.classroom
        assert set(updated_teacher.assigned_subjects.all()) == set(
            self.assigned_subjects
        )

    def test_update_teacher_profile_as_a_teacher_permission_denied(self):
        teacher = Teacher.objects.get(id=1)
        data = {
            "classroom": self.classroom.pk,
            "assigned_subjects": [subject.pk for subject in self.assigned_subjects],
        }
        response = self.client.patch(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            data=data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        updated_teacher = Teacher.objects.get(id=teacher.id)
        assert updated_teacher.classroom != self.classroom
        assert set(updated_teacher.assigned_subjects.all()) != set(
            self.assigned_subjects
        )

    def test_update_teacher_profile_as_a_student_permission_denied(self):
        teacher = Teacher.objects.get(id=1)
        data = {
            "classroom": self.classroom.pk,
            "assigned_subjects": [subject.pk for subject in self.assigned_subjects],
        }
        response = self.client.patch(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            data=data,
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.student_token}",
        )

        assert response.status_code == status.HTTP_403_FORBIDDEN
        updated_teacher = Teacher.objects.get(id=teacher.id)
        assert updated_teacher.classroom != self.classroom
        assert set(updated_teacher.assigned_subjects.all()) != set(
            self.assigned_subjects
        )

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

    def test_delete_teacher_profile_as_an_admin(self):
        teacher = Teacher.objects.get(id=1)
        print(teacher)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.admin_token}",
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Teacher.objects.filter(id=teacher.pk).exists()

    def test_delete_teacher_profile_a_teacher_permission_denied(self):
        teacher = Teacher.objects.get(id=1)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.teachers_token}",
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Teacher.objects.filter(id=teacher.pk).exists()

    def test_delete_teacher_profile_a_student_permission_denied(self):
        teacher = Teacher.objects.get(id=1)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            format="json",
            HTTP_AUTHORIZATION=f"Token {self.student_token}",
        )
        assert response.status_code == status.HTTP_403_FORBIDDEN
        assert Teacher.objects.filter(id=teacher.pk).exists()

    def test_delete_teacher_profile_without_authorization(self):
        teacher = Teacher.objects.get(id=1)

        response = self.client.delete(
            reverse("core:teachers-detail", kwargs={"pk": teacher.pk}),
            format="json",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Teacher.objects.filter(id=teacher.pk).exists()
