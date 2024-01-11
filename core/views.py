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
    """
    Django ModelViewSet: SubjectViewSet

    ViewSet for Subject model with CRUD operations and permissions based on user roles.

    Attributes:
        - queryset: All instances of the Subject model.
        - serializer_class: Serializer used for Subject model.
        - filter_backends: Uses DjangoFilterBackend for filtering.
        - filterset_class: Specifies the filter class to use.

    Methods:
        - get_permissions(self): Overrides the default permissions based on the action.
          - For create, destroy, update, and partial_update actions, requires IsTeacherOrAdmin permission.
          - For other actions, requires IsAuthenticated permission.

    Example Usage:
        - Manages CRUD operations for Subject model with specific permissions for certain actions.
    """

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
    """
    Django ModelViewSet: ClassRoomViewSet

    ViewSet for ClassRoom model with CRUD operations and permissions for teachers and admins.

    Attributes:
        - queryset: All instances of the ClassRoom model.
        - serializer_class: Serializer used for ClassRoom model.
        - permission_classes: Requires IsTeacherOrAdmin permission for all actions.

    Example Usage:
        - Manages CRUD operations for ClassRoom model with permissions restricted to teachers and admins.
    """

    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [IsTeacherOrAdmin]


class TeacherViewSet(ModelViewSet):
    """
    Django ModelViewSet: TeacherViewSet

    ViewSet for Teacher model with CRUD operations, custom actions, and permissions based on user roles.

    Attributes:
        - queryset: All instances of the Teacher model.

    Methods:
        - get_serializer_class(self): Determines the serializer class based on the action.
          - Uses TeacherSerializer for list and retrieve actions, otherwise uses TeacherSerializer2.
        - get_permissions(self): Overrides the default permissions based on the action.
          - For create, destroy, partial_update, and update actions, requires IsAdmin permission.
          - For other actions, requires IsAuthenticated permission.

    Custom Actions:
        - get_assigned_subjects(self, request): Retrieves and returns subjects assigned to the teacher.
          - Requires the teacher to be authenticated and associated with a user.
          - Returns a 404 response if the teacher or subjects are not found.
          - Uses SubjectSerializer to serialize and return the assigned subjects.

    Example Usage:
        - Manages CRUD operations for Teacher model with custom actions and specific permissions.
    """

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
    """
    Django ModelViewSet: StudentViewSet

    ViewSet for Student model with CRUD operations, custom actions, filtering, and permissions based on user roles.

    Attributes:
        - queryset: All instances of the Student model.
        - filter_backends: Uses DjangoFilterBackend for filtering.
        - filterset_class: Specifies the filter class to use.

    Methods:
        - get_serializer_class(self): Determines the serializer class based on the action.
          - Uses StudentSerializer for list and retrieve actions, otherwise uses StudentSerializer2.
        - get_permissions(self): Overrides the default permissions based on the action.
          - For create, destroy, update, and partial_update actions, requires IsTeacherOrAdmin permission.
          - For other actions, requires IsAuthenticated permission.

    Custom Actions:
        - get_enrolled_subjects(self, request): Retrieves and returns subjects enrolled by the student.
          - Requires the student to be authenticated and associated with a user.
          - Returns a 404 response if the student or subjects are not found.
          - Uses SubjectSerializer to serialize and return the enrolled subjects.

    Example Usage:
        - Manages CRUD operations for Student model with custom actions, filtering, and specific permissions.
    """

    queryset = Student.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = StudentFilter

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
    """
    Django ModelViewSet: AdminViewSet

    ViewSet for Admin model with CRUD operations and permissions restricted to admin users.

    Attributes:
        - queryset: All instances of the Admin model.
        - serializer_class: Serializer used for Admin model.
        - permission_classes: Requires IsAdmin permission for all actions.

    Example Usage:
        - Manages CRUD operations for Admin model with permissions restricted to admin users.
    """

    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [IsAdmin]


class ExamViewSet(ModelViewSet):
    """
    Django ModelViewSet: ExamViewSet

    ViewSet for Exam model with CRUD operations and permissions for teachers and admins.

    Attributes:
        - queryset: All instances of the Exam model.
        - serializer_class: Serializer used for Exam model.
        - permission_classes: Requires IsTeacherOrAdmin permission for all actions.

    Custom List Action:
        - list(self, request, *args, **kwargs): Overrides the default list action.
          - Checks if the queryset is empty and provides appropriate responses.
            - If query parameters are provided but no matches are found, returns a 404 response.
            - If no query parameters are provided and no exams are in the database, returns a 200 response.

    Example Usage:
        - Manages CRUD operations for Exam model with specific permissions and custom list action.
    """

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
    """
    Django ModelViewSet: SubjectResultViewSet

    ViewSet for SubjectResult model with CRUD operations and permissions for teachers and admins.

    Attributes:
        - queryset: All instances of the SubjectResult model.
        - serializer_class: Serializer used for SubjectResult model.
        - permission_classes: Requires IsTeacherOrAdmin permission for all actions.

    Custom List Action:
        - list(self, request, *args, **kwargs): Overrides the default list action.
          - Checks if the queryset is empty and provides appropriate responses.
            - If query parameters are provided but no matches are found, returns a 404 response.
            - If no query parameters are provided and no subject results are in the database, returns a 200 response.

    Example Usage:
        - Manages CRUD operations for SubjectResult model with specific permissions and custom list action.
    """

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
