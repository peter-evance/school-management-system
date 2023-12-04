from django.urls import path, include
from rest_framework import routers

from core.views import ClassRoomViewSet, SubjectViewSet

app_name = 'core'


router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'classrooms', ClassRoomViewSet, basename='classrooms')

urlpatterns = [
    path("", include(router.urls)),
]