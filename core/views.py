from core.filters import StudentFilter, SubjectFilter
from core.models.student import Student
from core.permissions import *
from core.serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import MethodNotAllowed


class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SubjectFilter

    def get_permissions(self):
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permission_classes = [IsTeacherOrAdmin]

        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ClassRoomViewSet(ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsTeacherOrAdmin]


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return TeacherSerializer
        return TeacherSerializer2

    def get_permissions(self):
        if self.action in ["create", "destroy", "partial_update", "update"]:
            permission_classes = [IsAdmin]

        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["GET"])
    def get_assigned_subjects(self, request):
        try:
            user = CustomUser.objects.get(id=request.user.id)
            teacher = Teacher.objects.get(user=user.id)
        except Teacher.DoesNotExist:
            return Response(
                {"detail": "Teacher not found, no subjects to display!"}, status=404
            )

        assigned_subjects = teacher.assigned_subjects.all()

        # You can serialize the subjects or use your custom serializer
        serializer = SubjectSerializer(assigned_subjects, many=True)

        return Response(serializer.data, status=200)


    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter
    # permission_classes = [IsTeacherOrAdmin]
    def get_permissions(self):
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permission_classes = [IsTeacherOrAdmin]

        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentSerializer
        return StudentSerializer2

    @action(detail=False, methods=["GET"])
    def get_enrolled_subjects(self, request):
        try:
            user = CustomUser.objects.get(id=request.user.id)
            student = Student.objects.get(user=user.id)
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


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    permission_classes = [IsTeacherOrAdmin]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            if request.query_params:
                # If query parameters are provided, but there are no matchers
                return Response(
                    {"detail": "No exams found matching the provided filters."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            else:
                # If no query parameters are provided, and there are no exams in the database
                return Response(
                    {"detail": "No Exams found in the farm yet."},
                    status=status.HTTP_200_OK,
                )

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SubjectResultViewSet(ModelViewSet):
    queryset = SubjectResult.objects.all()
    serializer_class = SubjectResultSerializer
    permission_classes = [IsTeacherOrAdmin]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset.exists():
            if request.query_params:
                # If query parameters are provided, but there are no matchers
                return Response(
                    {"detail": "No result found matching the provided filters."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            else:
                # If no query parameters are provided, and there are no subject result in the database
                return Response(
                    {"detail": "No result found in the database yet."},
                    status=status.HTTP_200_OK,
                )

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
