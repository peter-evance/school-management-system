from core.filters import StudentFilter, SubjectFilter
from core.models.student import Student
from core.permissions import *
from core.serializers import *
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SubjectFilter

    def get_permissions(self):
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permission_classes = [IsTeacherOrAdmin]

        else:
            permission_classes = [IsTeacher]
        return [permission() for permission in permission_classes]


class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsTeacherOrAdmin]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin]

    @action(detail=False, methods=["GET"])
    def get_assigned_subjects(self, request):
        try:
            user= CustomUser.objects.get(id=request.user.id)
            teacher = Teacher.objects.get(id=1)
        except Teacher.DoesNotExist:
            return Response(
                {"detail": "Teacher not found, no subjects to display!"}, status=404
            )

        assigned_subjects = teacher.assigned_subjects.all()

        # You can serialize the subjects or use your custom serializer
        serializer = SubjectSerializer(assigned_subjects, many=True)

        return Response(serializer.data, status=200)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacherOrAdmin]

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter

    @action(detail=False, methods=["GET"])
    def get_enrolled_subjects(self, request):
        try:
            user= CustomUser.objects.get(id=request.user.id)
            student = Student.objects.get(id=4)
        except Student.DoesNotExist:
            return Response(
                {"detail": "Student not found, no subjects to display!"}, status=404
            )

        enrolled_subjects = student.enrolled_subjects.all()

        # You can serialize the subjects or use your custom serializer
        serializer = SubjectSerializer(enrolled_subjects, many=True)

        return Response(serializer.data, status=200)

class AdminViewSet(ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdmin]
