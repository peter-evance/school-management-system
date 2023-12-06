from core.models.student import Student
from core.serializers import StudentSerializer
from core.models.classroom import ClassRoom
from core.models.subject import Subject
import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestSubjectViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_test_data):
        self.client = setup_users['client']
        self.teachers_token = setup_users['teacher_token']
        self.student_token = setup_users['student_token']
        self.admin_token = setup_users['admin_token']
        self.subject_data = setup_test_data['subject_data']
        self.classroom_data = setup_test_data['classroom_data']
        # self.student_objects= setup_test_data['student_objects']

    """ ADD SUBJECTS (POST)"""
    def test_add_subject_with_no_authentication(self):
        ''' This returns unauthorised user 401 '''
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json')
        print(response.data)
        assert response.status_code == 401
        assert not Subject.objects.filter(title = self.subject_data['title'])

    def test_add_subject_as_a_teacher(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}",)
        assert response.status_code == 201
        assert Subject.objects.all()

    def test_get_subject_with_authorizarion(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.teachers_token}", 
                                   follow=True)
        assert response.status_code == 200
    
    def test_add_subject_as_an_admin(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}",)
        assert response.status_code == 201
        assert Subject.objects.all()


    """ RETRIEVE SUBJECT (GET)"""
    def test_get_subject_with_no_authorizarion_unauthorized(self):
        ''' This returns unauthorised user 401 '''
        response = self.client.get(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    )
        assert response.status_code == 401

    def test_get_subject_as_a_teacher(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
        assert response.status_code == 200

    def test_get_subject_as_an_admin(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.admin_token}", 
                                   follow=True)
        assert response.status_code == 200

    def test_get_subject_as_a_student_permission_denied(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.student_token}")
        assert response.status_code == 403

    """ ADD CLASSROOM (POST)"""
    def test_add_classroom_as_a_teacher(self):
        from core.models.classroom import ClassRoom
        response = self.client.post(reverse('core:classrooms-list'), 
                                    self.classroom_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.teachers_token}",)
        assert response.status_code == 201
        assert ClassRoom.objects.all()

    def test_add_classroom_as_a_admin(self):
        from core.models.classroom import ClassRoom
        response = self.client.post(reverse('core:classrooms-list'), 
                                    self.classroom_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}",)
        assert response.status_code == 201
        assert ClassRoom.objects.all()
        
    def test_add_classroom_as_a_student_permission_denied(self):
        from core.models.classroom import ClassRoom
        response = self.client.post(reverse('core:classrooms-list'), 
                                    self.classroom_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.student_token}",)
        assert response.status_code == 403
        assert not ClassRoom.objects.all()


    """ RETRIEVE CLASSROOM (GET)"""
    def test_get_classroom_with_no_authentication_unauthorized(self):
        ''' This returns unauthorised user 401 '''
        response = self.client.get(reverse('core:classrooms-list'),format='json')
        assert response.status_code == 401

    def test_get_classrooms_as_a_teacher(self):
        ClassRoom.objects.create(**self.classroom_data)
        response = self.client.get(reverse('core:classrooms-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.teachers_token}")
        assert response.status_code == 200

    def test_get_subject_as_an_admin(self):
        ClassRoom.objects.create(**self.classroom_data)
        response = self.client.get(reverse('core:classrooms-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.admin_token}", 
                                   follow=True)
        assert response.status_code == 200

    def test_get_classroom_as_a_student_permission_denied(self):
        ClassRoom.objects.create(**self.classroom_data)
        response = self.client.get(reverse('core:classrooms-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.student_token}")
        assert response.status_code == 403

    """ VIEW INDIVIDUAL STUDENT (GET)"""
