from core.models.subject import Subject
import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestSubjectViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_subject_data):
        self.client = setup_users['client']
        self.teachers_token = setup_users['teacher_token']
        self.student_token = setup_users['student_token']
        self.admin_token = setup_users['admin_token']
        self.subject_data = setup_subject_data
        # self.classroom_data = setup_classroom_data


    def test_add_subject_with_no_authorizarion(self):
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

    def test_get_subject_as_a_teacher_with_authorizarion(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.teachers_token}", 
                                   follow=True)
        assert response.status_code == 200
        
    """ ADMIN """
    def test_add_subject_as_an_admin(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.admin_token}",)
        assert response.status_code == 201
        assert Subject.objects.all()

    def test_get_subject_as_an_admin(self):
        Subject.objects.create(**self.subject_data)
        response = self.client.get(reverse('core:subjects-list'), 
                                   HTTP_AUTHORIZATION=f"Token {self.admin_token}", 
                                   follow=True)
        assert response.status_code == 200
        print(response.data)



























@pytest.mark.django_db
class TestClassRoomViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_subject_data):
        self.client = setup_users['client']
        self.teachers_token = setup_users['teacher_token']
        self.student_token = setup_users['student_token']
        self.admin_token = setup_users['admin_token']
        self.subject_data = setup_subject_data

    # def test_add_new_classroom(self):
    #     response = self.client.post(reverse('core:classrooms-list'), 
    #                                 self.classroom_data, format='json',
    #                                 HTTP_AUTHORIZATION=f"Token {self.token}")
    #     assert response.status_code == 201
    #     assert 'code' in response.data
    #     print('================== Classroom ===================')
    #     print(response.data)

    # """
    # get classroom list as an authenticated user
    # here, the response.data is returning []
    # """
    # def test_get_classroom_list(self):
    #     response = self.client.get(reverse('core:classrooms-list'),
    #                                 HTTP_AUTHORIZATION=f"Token {self.token}")
    #     # assert response.data != []
    #     print('================== Classroom ===================')
    #     print(response.data)