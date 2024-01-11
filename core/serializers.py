from core.models.results import SubjectResult
from core.models.exams import Exam
from users.models import CustomUser
from core.models.admin import Admin
from core.models.student import Student
from core.models.teacher import Teacher
from core.models.classroom import ClassRoom
from core.models.subject import Subject
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    ReadOnlyField,
)
from users.serializers import CustomUserSerializer, CustomUserSerializer2


class SubjectSerializer(ModelSerializer):
    """
    Django Model Serializer: SubjectSerializer

    Serializes Subject model fields including id, title, code, class_room, and added_at.
    """

    class_room = PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())

    class Meta:
        model = Subject
        fields = ["id", "title", "code", "class_room", "added_at"]


class ClassRoomSerializer(ModelSerializer):
    """
    Django Model Serializer: ClassRoomSerializer

    Serializes ClassRoom model fields including id, title, code, capacity, and stream with nested representation.
    """

    class Meta:
        depth = True
        model = ClassRoom
        fields = ["id", "title", "code", "capacity", "stream"]


class TeacherSerializer(ModelSerializer):
    """
    Django Model Serializer: TeacherSerializer

    Serializes Teacher model fields including id, user (serialized with CustomUserSerializer),
    classroom, created_at, and assigned_subjects with one level of nested representation.
    """

    user = CustomUserSerializer()

    class Meta:
        depth = 1
        model = Teacher
        fields = ["id", "user", "classroom", "created_at", "assigned_subjects"]


class TeacherSerializer2(ModelSerializer):
    """
    Django Model Serializer: TeacherSerializer2

    Serializes Teacher model fields including id, user (serialized with CustomUserSerializer),
    classroom, created_at, and assigned_subjects without nested representation.
    """

    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user", "classroom", "created_at", "assigned_subjects"]


class StudentSerializer(ModelSerializer):
    """
    Django Model Serializer: StudentSerializer

    Serializes Student model fields including id, user (serialized with CustomUserSerializer),
    classroom, created_at, enrolled_subjects, and registration_number with one level of nested representation.
    """

    user = CustomUserSerializer()

    class Meta:
        depth = 1
        model = Student
        fields = [
            "id",
            "user",
            "classroom",
            "created_at",
            "enrolled_subjects",
            "registration_number",
        ]


class StudentSerializer2(ModelSerializer):
    """
    Django Model Serializer: StudentSerializer2

    Serializes Student model fields including id, user (serialized with CustomUserSerializer),
    classroom, created_at, enrolled_subjects, and registration_number without nested representation.
    """

    user = CustomUserSerializer()

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "classroom",
            "created_at",
            "enrolled_subjects",
            "registration_number",
        ]


class AdminSerializer(ModelSerializer):
    """
    Django Model Serializer: AdminSerializer

    Serializes Admin model fields including user and created.
    """

    class Meta:
        model = Admin
        fields = ["user", "created"]


class ExamSerializer(ModelSerializer):
    """
    Django Model Serializer: ExamSerializer

    Serializes Exam model fields including exam_type, subject, scheduled_date, duration,
    max_marks, and instructions."""

    class Meta:
        model = Exam
        fields = (
            "exam_type",
            "subject",
            "scheduled_date",
            "duration",
            "max_marks",
            "instructions",
        )


class SubjectResultSerializer(ModelSerializer):
    """
    Django Model Serializer: SubjectResultSerializer

    Serializes SubjectResult model fields including student, exam, marks_obtained, and remarks.
    """

    class Meta:
        model = SubjectResult
        fields = ("student", "exam", "marks_obtained", "remarks")
