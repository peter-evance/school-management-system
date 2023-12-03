from django.urls import path, include
from rest_framework import routers

from core.views import SubjectViewSet

app_name = 'core'


router = routers.DefaultRouter()
router.register(r'subjects', SubjectViewSet, basename='subjects')

urlpatterns = [
    path("", include(router.urls))
]