import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestSubjectViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_subject_data):
        self.client = setup_users['client']
        self.token = setup_users['token']
        self.subject_data = setup_subject_data
        # self.classroom_data = setup_classroom_data
    
    def test_add_subject_as_a_teacher(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.token}",)
        print(response.data)

    # def test_get_subject_as_a_teacher_with_authorizarion(self):
    #     response = self.client.get(reverse('core:subjects-list'), 
    #                                HTTP_AUTHORIZATION=f"Token {self.token}", 
    #                                follow=True)
    #     assert response.status_code == 200
    #     assert 'code' in response.data 
    #     print(response.data)

    def test_add_subject_as_a_teacher_with_no_authorizarion(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json')
        print(response.data)

    def test_get_subject_as_a_teacher_with_no_authorizarion(self):
        response = self.client.get(reverse('core:subjects-list'))
        print(response.data)

@pytest.mark.django_db
class TestClassRoomViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_classroom_data):
        self.client = setup_users['client']
        self.token = setup_users['token']
        self.classroom_data = setup_classroom_data

    def test_add_new_classroom(self):
        response = self.client.post(reverse('core:classrooms-list'), 
                                    self.classroom_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.token}")
        assert response.status_code == 201
        assert 'code' in response.data
        print('================== Classroom ===================')
        print(response.data)

    """
    get classroom list as an authenticated user
    here, the response.data is returning []
    """
    def test_get_classroom_list(self):
        response = self.client.get(reverse('core:classrooms-list'),
                                    HTTP_AUTHORIZATION=f"Token {self.token}")
        # assert response.data != []
        print('================== Classroom ===================')
        print(response.data)