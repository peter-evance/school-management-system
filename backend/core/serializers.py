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
    class_room = PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())

    class Meta:
        model = Subject
        fields = ["id", "title", "code", "class_room", "added_at"]


class ClassRoomSerializer(ModelSerializer):
    class Meta:
        depth = True
        model = ClassRoom
        fields = ["id", "title", "code", "capacity", "stream"]


class TeacherSerializer(ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        depth = 1
        model = Teacher
        fields = ["id", "user", "classroom", "created_at", "assigned_subjects"]


class TeacherSerializer2(ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Teacher
        fields = ["id", "user", "classroom", "created_at", "assigned_subjects"]


class StudentSerializer(ModelSerializer):
    user = CustomUserSerializer()
    # classroom = PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())

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
    class Meta:
        model = Admin
        fields = ["user", "created"]


class ExamSerializer(ModelSerializer):
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
    class Meta:
        model = SubjectResult
        fields = ("student", "exam", "marks_obtained", "remarks")
