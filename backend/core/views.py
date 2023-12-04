from core.models.classroom import ClassRoom
from core.permissions import IsTeacher
from core.models.subject import Subject
from core.serializers import *
from rest_framework import viewsets

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsTeacher]

class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsTeacher]