from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import routers

from users.views import CustomUserViewSet

app_name = 'users'


router = routers.DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='users')


urlpatterns = [
    path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="logout"),
    path("", include(router.urls))
]