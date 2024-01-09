from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import routers

from users.views import CustomUserViewSet, ProfileImageViewSet

app_name = "users"


router = routers.DefaultRouter()
router.register(r"users", CustomUserViewSet, basename="users")
router.register(r"profile-image", ProfileImageViewSet, basename="profile-image")

urlpatterns = [
    path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="logout"),
    path("", include(router.urls)),
]