from users.serializers import CustomUserSerializer
from users.serializers import CustomUserCreateSerializer
from users.models import CustomUser
import pytest
from core.choices import *
from core.models.student import Student
from core.serializers import ClassRoomSerializer, StudentSerializer, SubjectSerializer
from rest_framework import status
from core.models.classroom import ClassRoom
from core.models.subject import Subject
from django.urls import reverse

# @pytest.mark.django_db
# class TestSubjectViewSet:
#     @pytest.fixture(autouse=True)
#     def setup(self, setup_users, setup_subject_data):
#         self.client = setup_users['client']
#         self.teachers_token = setup_users['teacher_token']
#         self.student_token = setup_users['student_token']
#         self.admin_token = setup_users['admin_token']
#         self.subject_data = setup_subject_data

#     # return CustomUser.objects.create(**data)
#     def create_and_save(self):
#         """ This method serializes and save classroom object """
#         serializer = SubjectSerializer(data=self.subject_data)
#         assert serializer.is_valid(), serializer.errors
#         subject = serializer.save()
#         return subject
    
#     """ ADD SUBJECTS (POST)"""
#     def test_add_subject_as_a_teacher(self):
#         response = self.client.post(reverse('core:subjects-list'), 
#                                     self.subject_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.teachers_token}",)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Subject.objects.all()

#     def test_add_subject_as_an_admin(self):
#         response = self.client.post(reverse('core:subjects-list'), 
#                                     self.subject_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.admin_token}",)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert Subject.objects.all()
    
#     def test_add_subject_as_a_student_permission_denied(self):
#         response = self.client.post(reverse('core:subjects-list'), 
#                                     self.subject_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.student_token}",)
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_add_subject_with_no_authorizarion_unauthorized(self):
#         ''' This returns unauthorised user 401 '''
#         response = self.client.post(reverse('core:subjects-list'), 
#                                     self.subject_data, format='json')
#         print(response.data)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert not Subject.objects.filter(title = self.subject_data['title'])
    
#     """ RETRIEVE SUBJECT (GET)"""
#     def test_view_subject_as_a_teacher(self):
#         Subject.objects.create(**self.subject_data)
#         response = self.client.get(reverse('core:subjects-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_subject_as_an_admin(self):
#         Subject.objects.create(**self.subject_data)
#         response = self.client.get(reverse('core:subjects-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}", 
#                                    follow=True)
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_subject_as_a_student_permission_denied(self):
#         Subject.objects.create(**self.subject_data)
#         response = self.client.get(reverse('core:subjects-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
    
#     def test_view_subject_with_no_authorizarion_unauthorized(self):
#         ''' This returns unauthorised user 401 '''
#         response = self.client.get(reverse('core:subjects-list'), 
#                                     self.subject_data, format='json',
#                                     )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ RETRIEVE SUBJECT DETAILS (GET)"""
#     def test_view_subject_details_as_an_admin(self):
#         subject = self.create_and_save()
#         response = self.client.get(reverse('core:subjects-detail', kwargs={'pk':subject.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == subject.title

#     def test_view_subject_details_as_a_teacher(self):
#         subject = self.create_and_save()
#         response = self.client.get(reverse('core:subjects-detail', kwargs={'pk':subject.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == subject.title

#     def test_view_subject_details_as_a_student_permission_denied(self):
#         subject = self.create_and_save()
#         response = self.client.get(reverse('core:subjects-detail', kwargs={'pk':subject.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_view_subject_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         subject = self.create_and_save()
#         response = self.client.get(reverse('core:subjects-detail', kwargs={'pk':subject.pk}))
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ UPDATE SUBJECT (PATCH)"""
#     def test_update_subject_details_as_an_admin(self):
#         subject = self.create_and_save()
#         data = {'code': 'GST'}
#         response = self.client.patch(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == subject.title
#         assert Subject.objects.get(pk=subject.pk).code == 'GST'

#     def test_update_subject_details_as_a_teacher(self):
#         subject = self.create_and_save()
#         data = {'code': 'GST'}
#         response = self.client.patch(reverse('core:subjects-detail', kwargs={'pk':subject.pk}), data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == subject.title
#         assert Subject.objects.get(pk=subject.pk).code == 'GST'

#     def test_update_subject_details_as_a_student_permission_denied(self):
#         subject = self.create_and_save()
#         data = {'code': 'GST'}
#         response = self.client.patch(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert Subject.objects.get(pk=subject.pk).code != 'GST'

#     def test_update_subject_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         subject = self.create_and_save()
#         data = {'code': 'GST'}
#         response = self.client.patch(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),data=data,format='json',)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert Subject.objects.get(pk=subject.pk).code != 'GST'


#     """ DELETE SUBJECT (DELETE)"""
#     def test_delete_subject_details_as_an_admin(self):
#         subject = self.create_and_save()

#         response = self.client.delete(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_as_a_teacher(self):
#         subject = self.create_and_save()

#         response = self.client.delete(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_as_a_student_permission_denied(self):
#         subject = self.create_and_save()

#         response = self.client.delete(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert Subject.objects.filter(pk=subject.pk).exists()

#     def test_delete_subject_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         subject = self.create_and_save()

#         response = self.client.delete(reverse('core:subjects-detail', kwargs={'pk':subject.pk}),format='json',)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert Subject.objects.filter(pk=subject.pk).exists()


# """ TEST CLASSROOM VIEWSET """
# @pytest.mark.django_db
# class TestClassRoomViewSet:
#     @pytest.fixture(autouse=True)
#     def setup(self, setup_users, setup_classroom_data):
#         self.client = setup_users['client']
#         self.teachers_token = setup_users['teacher_token']
#         self.student_token = setup_users['student_token']
#         self.admin_token = setup_users['admin_token']
#         self.classroom_data = setup_classroom_data

#     def create_and_save(self):
#         """ This method serializes and save classroom object """
#         serializer = ClassRoomSerializer(data=self.classroom_data)
#         assert serializer.is_valid(), serializer.errors
#         classroom = serializer.save()
#         return classroom

#     """ ADD CLASSROOM (POST)"""
#     def test_add_classroom_as_a_teacher(self):
#         response = self.client.post(reverse('core:classrooms-list'), 
#                                     self.classroom_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.teachers_token}",)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert ClassRoom.objects.all()

#     def test_add_classroom_as_an_admin(self):
#         response = self.client.post(reverse('core:classrooms-list'), 
#                                     self.classroom_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.admin_token}",)
#         assert response.status_code == status.HTTP_201_CREATED
#         assert ClassRoom.objects.all()
    
#     def test_add_classroom_as_a_student_permission_denied(self):
#         response = self.client.post(reverse('core:classrooms-list'), 
#                                     self.classroom_data, format='json',
#                                     HTTP_AUTHORIZATION=f"Token {self.student_token}",)
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_add_classroom_with_no_authorization(self):
#         ''' This returns unauthorised user 401 '''
#         response = self.client.post(reverse('core:classrooms-list'), 
#                                     self.classroom_data, format='json')
#         print(response.data)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert not ClassRoom.objects.filter(title = self.classroom_data['code'])
    
#     """ RETRIEVE SUBJECT (GET)"""
#     def test_view_classroom_as_a_teacher(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(reverse('core:classrooms-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_classroom_as_an_admin(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(reverse('core:classrooms-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}", 
#                                    follow=True)
#         assert response.status_code == status.HTTP_200_OK

#     def test_view_classroom_as_a_student_permission_denied(self):
#         ClassRoom.objects.create(**self.classroom_data)
#         response = self.client.get(reverse('core:classrooms-list'), 
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
    
#     def test_view_classroom_with_no_authorizarion_unauthorized(self):
#         ''' This returns unauthorised user 401 '''
#         response = self.client.get(reverse('core:classrooms-list'), 
#                                     self.classroom_data, format='json',
#                                     )
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ RETRIEVE CLASSROOM DETAILS (GET)"""
#     def test_view_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()
#         response = self.client.get(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == classroom.title

#     def test_view_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()
#         response = self.client.get(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == classroom.title

#     def test_view_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()
#         response = self.client.get(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}), 
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN

#     def test_view_classroom_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         classroom = self.create_and_save()
#         response = self.client.get(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}))
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED

#     """ UPDATE CLASSROOM (PATCH)"""
#     def test_update_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()
#         data = {
#             'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             'code': ClassRoomCodeChoices.SSS_3
#             }
#         response = self.client.patch(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == data['title']
#         assert ClassRoom.objects.get(pk=classroom.pk).code ==  data['code']

#     def test_update_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()
#         data = {
#             'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             'code': ClassRoomCodeChoices.SSS_3
#             }
#         response = self.client.patch(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}), data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_200_OK
#         assert response.data['title'] == data['title']
#         assert ClassRoom.objects.get(pk=classroom.pk).code ==  data['code']

#     def test_update_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()
#         data = {
#             'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             'code': ClassRoomCodeChoices.SSS_3
#             }
#         response = self.client.patch(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),data=data,format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert ClassRoom.objects.get(pk=classroom.pk).title != data['title']
#         assert ClassRoom.objects.get(pk=classroom.pk).code != data['code']

#     def test_update_classroom_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         classroom = self.create_and_save()
#         data = {
#             'title': ClassRoomTitleChoices.SENIOR_SECONDARY_SCHOOL_3,
#             'code': ClassRoomCodeChoices.SSS_3
#             }
#         response = self.client.patch(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),data=data,format='json',)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert ClassRoom.objects.get(pk=classroom.pk).title != data['title']
#         assert ClassRoom.objects.get(pk=classroom.pk).code != data['code']


#     """ DELETE CLASSROOM (DELETE)"""
#     def test_delete_classroom_details_as_an_admin(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}")
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_as_a_teacher(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert not ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_as_a_student_permission_denied(self):
#         classroom = self.create_and_save()

#         response = self.client.delete(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),format='json',
#                                    HTTP_AUTHORIZATION=f"Token {self.student_token}")
#         assert response.status_code == status.HTTP_403_FORBIDDEN
#         assert ClassRoom.objects.filter(pk=classroom.pk).exists()

#     def test_delete_classroom_details_without_authorizarion(self):
#         ''' This returns unauthorised user 401 '''
#         classroom = self.create_and_save()
#         response = self.client.delete(reverse('core:classrooms-detail', kwargs={'pk':classroom.pk}),format='json',)
#         assert response.status_code == status.HTTP_401_UNAUTHORIZED
#         assert ClassRoom.objects.filter(pk=classroom.pk).exists()

""" UPDATE STUDENT PROFILE (POST) """
@pytest.mark.django_db
class TestStudentViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_student_data,):
        from rest_framework.test import APIClient
        self.client =  APIClient()
        self.teachers_token = setup_users['teacher_token']
        self.student_token = setup_users['student_token']
        self.admin_token = setup_users['admin_token']
        # self.student_profile = setup_student_profile_data['student_profile_data']
        # self.student_pk = setup_student_profile_data['user']
        self.student_data = setup_student_data
    
    def create_and_save(self,serializer):
        """ serializer method """
        assert serializer.is_valid(), serializer.errors
        return serializer.save(), serializer.errors
    
    def test_update_student_profile_as_a_teacher(self):  
        student_profile = self.create_and_save(CustomUserCreateSerializer(data=self.student_data))

        print(Student.objects.all())
        # print(student_profile)
        data = {
            'address':'2nd Avenue, Lagos, Ikeja'
        }     
        response = self.client.patch(reverse('core:students-detail', kwargs={'pk': student_profile.pk}),
                                    data=data,
                                    format='json',
                                    HTTP_AUTHORIZATION=f'Token {self.teachers_token}')
        # assert response.status_code == status.HTTP_200_OK
        print(response.data)
