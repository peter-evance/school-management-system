import pytest
from django.urls import reverse

@pytest.mark.django_db
class TestSubjectViewSet:
    @pytest.fixture(autouse=True)
    def setup(self, setup_users, setup_subject_data):
        self.client = setup_users['client']
        self.token = setup_users['token']
        self.subject_data = setup_subject_data
    
    def test_add_subject_as_a_teacher(self):
        response = self.client.post(reverse('core:subjects-list'), 
                                    self.subject_data, format='json',
                                    HTTP_AUTHORIZATION=f"Token {self.token}",)
        print(response.data)
