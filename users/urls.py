from django.urls import path, include
from djoser.views import TokenCreateView, TokenDestroyView
from rest_framework import routers

from users.views import CustomUserViewSet, NotificationViewSet, ProfileImageViewSet

app_name = "users"


router = routers.DefaultRouter()
router.register(r"profiles", CustomUserViewSet, basename="users")
router.register(r"profile-images", ProfileImageViewSet, basename="profile-image")
router.register(r"notifications", NotificationViewSet, basename="notification")

urlpatterns = [
    path("login/", TokenCreateView.as_view(), name="login"),
    path("logout/", TokenDestroyView.as_view(), name="logout"),
    path("", include(router.urls)),
]
