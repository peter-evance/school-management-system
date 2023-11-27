from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView

app_name = 'auth'

urlpatterns = [
    path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="logout"),
]