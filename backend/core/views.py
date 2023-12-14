from core.filters import StudentFilter, SubjectFilter
from core.models.student import Student
from core.permissions import *
from core.serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacherOrAdmin]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SubjectFilter


class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsTeacherOrAdmin]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin]


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacherOrAdmin]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter


class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdmin]
