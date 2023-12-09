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


class SubjectSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ["title", "code", "added_at"]


class ClassRoomSerializer(ModelSerializer):
    class Meta:
        model = ClassRoom
        fields = ["title", "code", "capacity", "stream"]


class TeacherSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    classroom = PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())
    assigned_subjects = PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), many=True
    )

    class Meta:
        # depth = True
        model = Teacher
        fields = ["user", "classroom", "created_at", "assigned_subjects"]


class StudentSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    classroom = PrimaryKeyRelatedField(queryset=ClassRoom.objects.all())
    enrolled_subjects = PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), many=True
    )

    class Meta:
        depth = True
        model = Student
        fields = [
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
