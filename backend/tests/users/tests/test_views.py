from django.http import HttpResponse
import pytest
from rest_framework.test import APIClient

from users.models import CustomUser

client = APIClient()


@pytest.mark.django_db
def test_user_flow(client):
    register_data ={
        'username':'michaelademic',
        'first_name': 'michael',
        'last_name': 'ademic',
        'sex': CustomUser.SexChoices.MALE,
        'role': CustomUser.RoleChoices.ADMIN,
        'password': '12345678QQ'
        }
    
    response = client.post("/auth/users/", register_data)
    assert response.status_code == 201
    assert response.data['username'] == 'michaelademic'
    print(response.data)