from django.urls import path, include
from rest_framework import routers

from core.views import *

app_name = 'core'


router = routers.DefaultRouter()
router.register(r'admin', AdminViewSet, basename='admin')
router.register(r'subjects', SubjectViewSet, basename='subjects')
router.register(r'students', StudentViewSet, basename='students')
router.register(r'classrooms', ClassRoomViewSet, basename='classrooms')
router.register(r'teachers', TeacherViewSet, basename='teachers')

urlpatterns = [
    path("", include(router.urls)),
]